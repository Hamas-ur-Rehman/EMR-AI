import os
import time
import ffmpeg
import dotenv
import gradio as gr
from prompts import *
from openai import OpenAI
from custom_logger import *
from langchain_community.document_loaders import UnstructuredPDFLoader
dotenv.load_dotenv()
client = OpenAI()


with gr.Blocks(title="EMR GENERATOR") as demo:
    gr.Markdown("## EMR GENERATOR")

    with gr.Row():
        with gr.Column(scale=3):
            audio_input = gr.Audio(label="Conversation Audio",sources=["upload"],type='filepath')
            previous_EMR = gr.File(label="Previous EMR",file_count='single',file_types=[".pdf"],type='filepath')
            model = gr.Dropdown(['gpt-4-1106-preview','gpt-4','gpt-3.5-turbo-1106',],label="Model",value='gpt-3.5-turbo-1106',interactive=True,container=False)
            
            generate = gr.Button(value="Generate EMR")
        
        with gr.Column(scale=6):
            with gr.Tab("GENERATE EMR"):
                with gr.Accordion():    
                    Output = gr.Markdown(value="",label="Status",visible=True)
            with gr.Tab("Transcription"):
                transcriptx = gr.Textbox(container=True,show_copy_button=True,interactive=False,label="Transcript",value="",visible=True,lines=20,)
            with gr.Tab("AI Prompt"):
                promptx = gr.Textbox(container=True,show_copy_button=True,interactive=True,label="Prompt",value=PRE_PROMPT,visible=True,lines=20,)
    
    def generate_EMR(audio,previous_EMR,PRE_=PRE_PROMPT,model='gpt-3.5-turbo-1106',progress=gr.Progress()):
        progress(0, "Recieving Files")
        if audio and previous_EMR:
            log.info(f"Audio File recieved: {audio}")
            log.info(f"Previous EMR recieved: {previous_EMR}")
            progress(0.2, "Files Recieved for processing")

            start = time.time()
            log.info("Extracting previous EMR text")
            progress(0.2, "Extracting previous EMR text")
            loader = UnstructuredPDFLoader(fr"{previous_EMR}")
            data = loader.load()
            previous_EMR_text = ""
            for i in data:
                previous_EMR_text += i.page_content + "\n"
            log.warning(f"Previous EMR extracted in {time.time()-start} seconds")

            start = time.time()
            log.info("Transcribing conversation audio")
            output_file = 'output.mp3'
            try:
                progress(0.5, "Converting audio to mp3")
                ffmpeg.input(fr"{audio}").output(output_file, format='mp3',y='-y').run()
                progress(0.7, "Transcribing audio conversation")
                transcript = client.audio.transcriptions.create(
                    model="whisper-1",
                    file=open(fr"{output_file}", "rb")
                )
                conversation_text = transcript.text
            except Exception as e:
                log.error(f"Error in transcribing audio: {e}")
                raise gr.Error(f"Error in transcribing audio: {e}")

            log.warning(f"Conversation audio transcribed in {time.time()-start} seconds")
            PROMPT = get_prompt(conversation_text,previous_EMR_text)
            
            start = time.time()
            log.info("Generating EMR")
            progress(0.9, "Generating EMR")
            try:
                response = client.chat.completions.create(
                    temperature = 0,
                    model=model,
                    messages=[
                        {"role": "system", "content": PRE_},
                        {"role": "system", "content": f"This is the examples to help you regarding which section you should be commenting on after these examples I will provide the previous EMR report and the current checkup transcript for you to utlize to generate the new EMT.\n These are the Examples {EXAMPLES} "},
                        {"role": "system", "content": f"This is just a scenario explaining everything to you as an example to help you understand the process of generating the EMR report. \n{EXTRA} "},
                        {"role": "system", "content": f"This is the previous EMR report for the patient and the current conversation transcript. \n{PROMPT}\n\nGo through this data carefully and be mindfful to fill in the sections that are necessary its important to not according to the data you may not want to add comments under every section you may want to put nil under some which may not be as needed according the the examples provided for your guidance "},
                        {"role": "user", "content": "GENERATE EMR"},
                    ]
                )
                log.warning(f"EMR generated in {time.time()-start} seconds")
                GENERATED_EMR = response.choices[0].message.content
            except Exception as e:
                log.error(f"Error in generating EMR: {e}")
                raise gr.Error(f"Error in generating EMR: {e}")
            try:
                os.remove('./output.mp3')
            except Exception as e:
                log.error(f"Error in removing audio file: {e}")
            return gr.Markdown(value=GENERATED_EMR,visible=True),gr.Textbox(value=conversation_text,visible=True,show_copy_button=True,container=True,label="Transcript",lines=20,)
        else:
            raise gr.Error("Please provide both conversation and previous EMR")

    generate.click(generate_EMR,[audio_input,previous_EMR,promptx,model],[Output,transcriptx])

demo.queue()
demo.launch()
