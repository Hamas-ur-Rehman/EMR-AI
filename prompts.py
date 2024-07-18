from datetime import datetime
def get_prompt(audiotranscript, emrreport):
    current_date = datetime.now().date()
    PROMPT = f"""Current Date: {current_date}
    These are the patient's audio transcription and previous EMR report:

    ---------------------------------------------------------
    PREVIOUS EMR REPORT
    ---------------------------------------------------------
    Previous EMR Report: [{emrreport}]

    
    ---------------------------------------------------------
    AUDIO TRANSCRIPTS
    ---------------------------------------------------------
    Conversation Audio: [{audiotranscript}]

    ---------------------------------------------------------
    You will be using the Audio Transcriptions to update the previous EMR Report with new thoughts.
    Heading should be followed with a new line and sections should be seperated with a new line and this '--------------------------------------'
    """
    return PROMPT

PRE_PROMPT ="""You are a helpful assistant which helps the user in generating an EMR Report (Electronic Medical Record)
    The user will provide you with a conversation audio transcription and a previous EMR report. You will use the conversation audio to understand the patient's current condition and use the previous EMR report to understand the patient's medical history. You will then generate a new EMR report based on the conversation audio and the previous EMR report.
    Make Sure to make the EMR detailed. Each section should atleast be 10 lines long.
    The EMR will contain the following sections:
    Section A: Intake/History
    Section B: Cognition
    Section C: Communication/Vision
    Section D: Mood/Behavior
    Section E: Psychosocial Well-Being
    Section F: Functional Status
    Section G: Continence
    Section H: Disease Diagnoses
    Section I: Health Conditions
    Section J: Nutritional
    Section K: Medications/Allergies
    Section L: Treatments/Procedures
    Section M: Social Supports
    Section N: Environmental

    The EMR should be generated in a clear and concise manner, and should be easy to understand for the patient and the healthcare provider. The EMR should be generated in a way that is consistent with the patient's medical history and the conversation audio transcription.
    The EMR should be structured in a proper way having all the sections mentioned above with your comments and suggestions based on the conversation audio and the previous EMR report.
    No need to add page numbers
    EMR heading should be BOLD and in CAPITALS

    I WILL BE SHARING THE INFORMATION ABOUT THE EXAMPLES NEXT YOU WILL USE THEM TO IDENTIFY WHICH SECTIONS ARE RELEVENT FOR THE EMR AND WHICH SECTION WILL GET COMMENTS AS NIL BUT ALL SECTIONS SHOULD BE LISTED.
"""

EXAMPLES = """
    --------------------------------------
    **Section A: Intake and History**

    **POLICY FOR THIS SECTION**
    (All documentation should not be all capital letters)
    - Who was present during the visit - indicate in the top section if applicable, Translator used (ID# for language line, family, and/or caregiver) and member agreed
    - Living situation
    - PCP (include last visit)
    - Ask about CDPAS interest or Has CDPAS
    - Justification for Social Day Care (SDC) if member is interested or currently attending.
    - Elevator and/or Stairs Present
    - For mutual cases, document name, CIN#, list services {days x hrs), and vendor

    **Examples Related to this Section:**
    1. "Member’s primary physician is Dr. Mona Peter (718 888 5555) and last visit was 4.25.2018. Member also sees a cardiologist, Dr. Amy Heart (212 529 4532), last visit on 5.10.2019 for ongoing heart condition management. Member’s PCA and Caregiver, John Doe (son), Heart to Heart agency (555-1234) was present during this assessment. Member is not enrolled in CDPAS. CDPAS discussed and member is not interested. Member is currently attending SDC due to needing assistance with ADLs/IADLs and to reduce social isolation. Mutual Case: Jane Doe, CIN# 123456789, receiving 3 days x 2 hrs of personal care from Loving Care agency."

    2. "Member is a 78 y/o Russian speaking morbidly obese male, with primary diagnosis of Rheumatoid arthritis. Member lives with his son in a 2-bedroom apartment located on the 4th floor of an elevator apartment building. Home is clean, clutter-free, well-lit, appropriate temperature, no infestations, and safe for home care services. PCP Dr. Mona Peter (718 888 5555) last visit was 4.25.2018. CDPAS discussed with member. He verbalized understanding and is not interested at this time. Member is satisfied with current services and plan of care through Heart to Heart agency."

    **Social Adult Day Care (SADC) Justification Documentation Examples:**
    1. SDC services assist the member with ADLs/IADLs, reduce social isolation, and increase social and community engagement to help the member achieve optimal physical and mental functioning.
    2. Member will continue to benefit from SDC to improve mood and mental state.
    3. By attending the social day care service, the member would benefit from interacting with others and participating in structured activities to prevent isolating/depressive feelings and delay deterioration of mental status. It also promotes socialization with people of the same age and cultural background.
    4. The member will benefit from the socialization and stimulation provided by the SADC. The member participates in music therapy sessions.

    **Additional Notes:**
    - RN observed 2 PCAs present during telehealth assessment. Daughter reported member's husband is getting service from another MLTC, refused to provide name, current service hour. Daughter became upset when RN asked further questions regarding member's husband. RN explained to daughter and member that we are your health plan and we are here to help take care of your mother's medical, social, psychological needs, so all these questions will help CM to deliver the best care possible. Member's daughter raised her voice, questioning why RN is asking all these personal questions and became uncooperative throughout the assessment. Information provided appeared to be inconsistent. When RN asked about specific care needs, the daughter reported one thing, but the member said another.
    --------------------------------------Certainly! Here's how the provided data can be formatted following the structure and style of the example given:

    --------------------------------------
    **Section B: Cognition**

    **POLICY FOR THIS SECTION**
    - Ensure the member is alert and oriented to person, place, and time.
    - Provide a description of the assessment findings to support Short-Term Memory (STM) and Procedural Memory problems.
    - Determine if the member is self-directing. Document tasks requiring assistance if the member can direct ADLs but needs help with some IADLs. Specify who directs care.
    - Assess if the member can recognize an emergency situation and/or activate 911 if necessary. Mention if there is a Personal Emergency Response System (PERS) in the home.
    - For responses indicating the member is Moderately, Severely impaired, or in a Coma: A comment is mandatory and must include clinical justification/explanation.

    **NOTE:** The RN must ensure that an informal caregiver is present during the interview or can be contacted by phone. The RN cannot conduct the interview with only the member’s PCA but needs to include a patient’s Health Care Provider (HCP) or representative.

    **Examples Related to this Section:**
    - "Member is alert and oriented x {1/2/3}, {disoriented to person/time/place}. Member {can, cannot} describe an emergency plan and call 911."
    - "Member {is/is not} self-directing. If the member can direct ADLs but needs assistance with some IADLs, document tasks requiring assistance. For example, 'Member does need medication reminders and total assist with bill paying and housekeeping. Member’s daughter manages finances including paying bills. Member is able to direct all ADLs'."
    - "Member {can, cannot} activate PERS. If the member could benefit from having PERS, then document 'Member would benefit from having PERS and was instructed on the advantages of having PERS'."
    - "Member is alert and oriented x 3, and at times, experiences episodes of forgetfulness, self-directing. Member can describe an emergency plan and call 911."
    - "Member’s cognitive decline is associated with {enter specific}. Example: advanced dementia, advanced Parkinson’s, uncontrolled diabetes, age-related cognitive decline, new living environment (recently hospitalized or admitted to NH), increased social isolation, new medication or change in medication dosage, sleep deprivation due to insomnia."
    - "Member has a diagnosis of {enter specific, i.e., Bipolar/Schizophrenia}, is medication compliant, and does make decisions related to ADLs and IADLs."

    --------------------------------------

    This format maintains the structure and detail of the provided examples, ensuring clarity and consistency in documenting cognitive assessments.--------------------------------------
    Section C: Communication / Vision

    **POLICY FOR THIS SECTION**
    - Document if the member uses any visual or hearing appliances.
    - Assess the adequacy of vision with the appliance and specify if communication and vision limitations are chronic or new.
    - Note any interventions or teachings provided for identified impairments.
    - For members who are legally blind, detail their navigation at home and outdoors, eating habits, medication management, and phone usage. Clarify if the blindness affects one or both eyes and describe any limitations in mobility and ADLs. Mention the duration of blindness and the activities the member can perform independently.

    Examples Related to this Section:
    1. "Member has been diagnosed with glaucoma. According to the member and their informal caregiver, the member is non-compliant with eye drop treatment and refuses to attend medical appointments. The member uses a {specify device, e.g., hearing aid, eyeglasses, magnifier} which improves their {vision/hearing}. The member is legally blind but not totally blind for over 5 years and is observed to navigate safely around the home. The member reports being able to go outdoors using a walking device safely. The PCA noted that the member can use the toilet without difficulty and there is no recent history of falls. The member also mentioned being able to make phone calls in emergencies and can take pre-poured/blister-packed medication as long as it is placed on the kitchen countertop on the right side."

    2. "The member wears glasses to read small print on medication bottles and uses a hearing aid for clearer hearing. With these appliances, both vision and hearing are considered adequate."

    3. "Assessment findings indicate a decline in {communication/vision}. The reason for the decline is related to {specific reason}. The member's ability to {make self-understood/understand others} has declined due to {specific reason}. Examples include advanced dementia, advanced Parkinson’s disease, uncontrolled diabetes, and age-related cognitive decline."
    ----------------------------------------------------------------------------
    Section D: Mood / Behavior

    **POLICY FOR THIS SECTION**
    If a response is other than "not present," then document the specific issue and interventions to improve outcomes.

    • Depressive symptoms noted during the visit?
    • Suicidal or Homicidal ideations and attempts to hurt self and others only if the episode is present. (add into Care Coordination Form)
    • Wandering episodes? Describe the incidence only if indicated. The member could wander in the bed (e.g., attempts to get out of bed and fell without realizing the safety issue multiple times)

    Examples Related to this Section:
    Member/family reported and/or RN observed {specific mood/behavioral issue}. The member has a diagnosis of {psych dx}, {not controlled, controlled with medications and/or psych therapy}. The member reported that treatment has been {helpful/not helpful} in alleviating {specific psychiatric condition, behaviors, etc.} symptoms.

    Interventions: RN notified {MD/specialist/family/CMT} of {observed/reported, specifics}. RN recommends {psych evaluation; and psychosocial assessment}. Instructed {member/informal caregiver} on the importance {of med compliance, psych therapy} {member/informal} verbalized {understanding, needs additional instruction}
    Educated caregivers on the importance of establishing a daily routine that is structured and predictable.
    RN discussed ways to reduce the incident of wandering since the member attempted to get out of bed and fell and got confused about where she is in the house. PCA reported the member would walk to the kitchen while attempting to go use the bathroom. {locks on exterior door, bed alarm}.

    Discussed MLTC social day benefit and member {is/isn’t} interested at this time.

    Member/informal caregiver reported {psychosocial issue}.
    Example: {Member/informal caregiver} reported feeling lonely and isolated causing {specifics} Examples: poor appetite and difficulty sleeping. The member has been feeling sad for several months due to {specifics} Example: death of a spouse, unable to see family members

    The member is {active with APS or member referred to APS}. APS case name is {enter SW name and phone #}.

    Recommend Care Manager follow up with the member to address the report of {specifics}
    Document if the Member is active with APS or if the member referred to APS. APS case name is {enter SW name and phone #}.

    Behavioral Symptoms {Member/informal caregiver} report {triggers = wandering, verbal abuse, physical abuse, socially inappropriate or disruptive behaviors, inappropriate public sexual behavior, resists care}

    Per {member/family} decline related to {enter reason i.e., decline in specific diagnosis, change in living arrangement, new medication, not sleeping, change in caregivers}.

    ----------------------------------------------------------------------------
    Section E: Psychosocial Well-Being

    **POLICY FOR THIS SECTION**
    Comments are mandatory if issues or problems are identified for the following questions: 
    1. Lonely
    2. Social
    3. Activities
    4. Time Alone

    **Lonely**: Conduct an extensive interview to determine if the member feels lonely and distressed if they indicate loneliness.

    **Time Spent Alone**: Reflects the time in the morning and afternoon. For example, if a PCA is in the home for 4 hours per day, then coding would reflect that the member is alone "more than 2 hours but less than 8 hours".

    Differentiate between loneliness and boredom. Document interventions and any education provided.

    - Current psych/mental health therapist contacts and last date of visit?
    - Current psych treatment regimen
    - Is member lonely (quality measure)
    - Any major life stressors? Describe the incident
    - SDC Discussion

    **Examples Related to this Section**:
    1. "Member does not have any current behavioral problems. Her anxiety is well managed, currently seeing Psychiatry: Dr. Mark Lone, CABS Health Medical Center 718 338 5678, visits every month. Last visit 4.12.2018 and mental health therapist Debbie at the same center weekly. Last visit 4.4.2018. Member denies loneliness. Member has a large family and everyone is very friendly and socializes a lot, especially over the weekend. Member lives with her son. 
    - **Interventions**: 
        - Recommend Care Manager follow up with member to address report of {enter specifics}
        - RN notified {MD/specialist/family/CMT} of {observed/reported} {enter specifics}. RN recommends {psych evaluation; and psychosocial assessment}.
        - Discussed services provided by SDC/ADHC. Member {is/isn’t} interested at this time.
        - Member is active with APS or member referred to APS. APS case name is {enter SW name and phone #}."

    2. "**Lonely**: Provided {member/informal caregiver} with information on the Friendship Line # 800 971-0016. Discussed with {member/informal caregiver} {Social, Adult Day Services Community Center} and contacting CM to review service options.
    - Example: {Member/informal caregiver} reported feeling lonely and has had problems with {poor appetite, difficulty sleeping, lack of interest in social activities}.  
    - {Member/informal caregiver} reported that member {had an episode of severe personal illness, the death or severe illness of a close family member or friend, the loss of the person’s home, a major loss of income or assets, being the victim of a crime such as robbery or assault, the loss of the person’s driving license or car}."

    3. "{Member/informal caregiver} reported that member {had an episode of severe personal illness, the death or severe illness of a close family member or friend, the loss of the person’s home, a major loss of income or assets, being the victim of a crime such as robbery or assault, the loss of the person’s driving license or car}."
    ----------------------------------------------------------------------------
    Section F: Functional Status

    **POLICY FOR THIS SECTION**
    Documentation must reflect specific functional limitations and how the member manages after service hours and on days without service. For members with IADL/ADL coding greater than "Independent" or "Independent set-up help," detailed descriptions of functional limitations and the required supervision or assistance are necessary. Equipment management should be noted except for members in nursing homes. Stair navigation ability and meal preparation capacity should be accurately documented. Any decline or improvement in functional abilities within a 90-day look back period must be compared to the last reassessment for accurate coding. Escort needs for medical appointments should also be indicated.

    1. **DME and Equipment in Home**: List all DMEs and/or equipment present as per Dr. Arnold's reference.
    2. **Stair Navigation**: Ability to use a full flight of stairs (12-14 steps at one time).
    3. **Managing Medications**: Specify the type of assistance needed and provided, with mandatory comments on supervision, limited, extensive, maximal, total dependence, or did not occur.
    4. **Walking/Locomotion**: Comments must include observations of ambulatory status, transferring, use of assistive devices, and type of DME equipment used.
    5. **Bed Mobility**: For extensive, maximal, total dependence, or activity did not occur, comments must outline the type of assistance needed, including turning, positioning, and moving in bed.
    6. **Change in ADL Status and Overall Self Sufficiency**: Indicate if there has been an improvement or decline in functional status or NFLOC score due to changes in health conditions from the previous assessment. Comments identifying areas of improvement/decline are required. If uncertain, an explanation must be provided.

    **Examples Related to this Section**:
    - DME includes cane, walker, wheelchair, shower chair, grab bars, commode, hospital bed. Member requires contact guarding with a walker, has difficulty with stairs, and needs assistance for steps outside the doctor’s office. Escort is needed for public transportation.
    - After the aide leaves, the member manages with pre-placed essentials and reports the ability to walk with difficulty and pain. The member's capacity for IADL tasks and equipment management should be detailed.
    - Questions to assess toileting abilities include the ability to use grab bars, hand clasping, and bending forward.
    - Document how the member manages key ADLs when the aide is not present and what has caused any improvements in ADLs since the last assessment.

    **Interventions and Recommendations**:
    - Members may benefit from PT referrals, scheduling PCP visits for evaluations, and specific DME for nighttime toilet use.
    - For continuous care needs, document how these needs are met when PCA is not available, including the use of commodes, diapers, urinals, chux, or family support.

    ----------------------------------------------------------------------------
    Section G: Continence

    **POLICY FOR THIS SECTION**
    General Information: For the elderly population, symptoms of urinary tract infection may include confusion, disorientation, agitation, poor motor skills, dizziness, falling, and sometimes even depression.

    1. Include nursing intervention and education for any level of incontinence chosen.
    2. Determine the type of incontinent supplies.
    3. For members who require hands-on assist with toileting: Frequency and interventions to manage toileting during the night.
    4. Document DME used to manage incontinence (i.e., grab bars and commode, diaper with amount).
    5. Document how toileting needs are met when the aide is not scheduled.
    6. If Total Incontinence is chosen and there is no corresponding/supportive diagnosis, a comment is mandatory explaining the reason for total incontinence.

    Examples Related to this Section:
    Member reported experiencing {bowel/bladder} incontinence. Member currently uses {pads/chux/diapers/undergarments}. Include the size of supplies used.

    Interventions: {Member/Informal Caregiver/PCA} educated on inspecting skin daily and keeping skin clean and dry and frequent changes of {pads/chux/diapers/undergarment to prevent skin breakdown}.
    Member has a {type of ostomy} in place from {ostomy brand and specifics}. Ostomy care is being provided by {member/caregiver/other levels of care}.

    ****If Member has a diagnosis of functional incontinence then document findings that support functional incontinence knows when needs to urinate but cannot always get to the bathroom. Member uses diapers to manage incontinence.

    Member requires intermittent catheter and {does/does not need} assistance.
    Member’s informal caregiver assists with toileting {between hrs of x and x} on {enter days of week}.

    Member instructed to see MD regarding the report of frequent urination.
    Discussed {bedside commode/urinal} to manage toileting at night.

    Educated {member/informal caregiver} regarding {bladder training – increasing the time between bladder voiding after getting the urge to go {i.e., increasing by 10-15 minutes until you are able to reach urinating every 2-4 hours); Double voiding – urinating once, then waiting a few minutes and trying again; scheduled toilet trips – to train oneself to urinate every 2-4 hours rather than waiting for the need to go}.

    Educated {member/informal caregiver} on fluid and dietary measures to improve urinary incontinence. Specific Examples: excessive weight puts pressure on your bladder; keeping a “bladder diary” to track foods/drinks consumed and urination schedule to see if there are any dietary triggers; limiting caffeine intake {i.e., coffee, soda, tea, Excedrin® migraine) since these increase bladder activity; limiting alcohol consumption {liquor, beer, wine) since these increase bladder activity and act as a diuretic, resulting in increased frequency of urination; limit water intake before bedtime however only do this under a provider’s supervision; limit spicy foods.

    Educated {member/informal caregiver} on {signs and symptoms of urinary tract infection and making an appointment with PCP. S/S include more frequent urination/urinary incontinence, burning with urination, low back pain, cloudy or change in the smell of urine}.

    Educated {member/informal caregiver} on the importance of keeping clean skin and dry, changing soiled items timely, escalate to PCP, referral to a specialist and nutritionist.

    Member is occasionally incontinent of urine due to BPH. The assessor provided teaching on timed voiding and instructed on male Kegel exercises at least 3 times a day. The member demonstrated understanding. Taught to limit liquids at night, manage caffeine intake. The member verbalized understanding. The member refuses incontinent supplies.
    ----------------------------------------------------------------------------
    Section H: Disease Diagnosis

    **POLICY FOR THIS SECTION**
    - Review MD order in EMR (e.g., 485 for PCA cases, DOH form for CDPAS) to capture Diagnoses.
    - Ensure to bubble (fill in the radio button) in the disease section H within the assessment to count towards the risk score. Do not just add ICD10 codes.
    - Document how the presence of these diseases affects the member's ADLs/IADLs, including any changes (improvement/decline) in diseases (e.g., DM, CHF, etc).
    - For conditions like Depression, Dialysis, etc., comments are mandatory (e.g., dialysis status, linked to mental health services, A1C levels if available).

    Examples Related to this Section:
    1. "Member reports a history of RA, multiple joint pain, DM II, HTN, and states there has been no change in these conditions since the last assessment. The member's ability to perform ADLs/IADLs remains consistent with previous evaluations. No new interventions have been introduced since the last review."
    2. "Member reports changes in blood sugar levels, ranging between xxx-xxx fasting/2 hours after eating in the past week, which is [better/worse/no change] since the last assessment. This change has [improved/worsened/no impact] on the member's ability to perform daily activities and manage their condition. The member is [not] currently linked to mental health services for support in managing their DM II."
    3. "The member, who is on dialysis, has shown [improvement/decline/no change] in their ability to perform ADLs/IADLs since the last assessment. The dialysis schedule has been [adjusted/maintained] to better accommodate the member's lifestyle and improve their overall well-being. A1C levels, if available, are [insert A1C levels], indicating [improvement/decline/stability] in the member's condition."

    ----------------------------------------------------------------------------
    Section I: Health Conditions

    **POLICY FOR THIS SECTION**

    **Falls**
    - Detail of recent fall: Member suffered a fall last month, resulting in a cut on his elbow while trying to break the fall. The incident occurred on 6/10 when the member slipped on a loose rug in the living room during the evening, after PCA hours, while walking to the bathroom. The cut wound has healed. No subsequent falls reported since the last month.
    - Intervention: Assessor instructed to remove the rug from the living room, ensure the home remains well-lit, and advised the member to walk cautiously through the home.

    **Pain**
    - Member reports arthritic pain in shoulders, hands, legs, arms, and back due to rheumatoid arthritis. The pain level is 4/10 on the pain scale.
    - Pain Management: Pain is controlled adequately by Meloxicam 5 mg daily. The member also rests in between activities to alleviate pain and schedules activities earlier in the morning right after taking medication.
    - Improvement: Member reports pain has improved since outpatient PT/home PT/increase dosage of pain medication/change to new pain medication. Pain scale was 6/10 and after PT and pain cream, it goes down to 3/10.

    **Dyspnea (Shortness of Breath - SOB)**
    - Member reports SOB with normal day-to-day activities, currently receiving treatment for a diagnosis of {insert diagnosis}. Member also reports SOB with moderate exertion {specify activity}. The SOB occurs {specify frequency} in the past 3 days.
    - Intervention: Educated {member/informal caregiver} on taking medications as ordered, and if symptoms worsen, to seek medical attention. {Member/Caregiver} verbalized understanding.
    - Additional Education: Instructed on the importance of keeping regularly scheduled MD appointments to monitor lung function, discussing with a doctor or respiratory therapist about techniques for breathing more efficiently throughout the day, and managing mucus collection. Advised on lifestyle changes such as losing weight, regular exercise, avoiding cigarette smoke and inhaled irritants, eating a healthy diet, drinking plenty of fluids, getting plenty of rest, reducing excess stress, and staying indoors during extreme heat and humidity using fans and air conditioning.

    **Examples Related to this Section:**
    - Fall Intervention: Instructed {member/caregiver/PCA} to use ambulatory devices when walking/transferring, keep home safer by removing tripping hazards, participate in physical activities to improve balance and coordination, and schedule appointments with PCP to review medications for side effects that could contribute to falls.
    - Pain Management: {Caregiver/member} instructed on fall precautions, removing clutter, wearing comfortable non-skid shoes, ensuring adequate lighting, and placing non-skid surfaces in and outside of the bathtub/shower. Reviewed medications for possible side effects contributing to falls. Advised on scheduling appointments with PCP before pain reaches emergency levels and discussing referral to a pain management specialist.
    - Dyspnea Management: Educated {member/informal caregiver} on the importance of taking daily medications/inhalers as prescribed, using oxygen as prescribed, avoiding cigarette smoke and inhaled irritants, continuing regular exercise, eating a healthy diet, drinking plenty of fluids, getting plenty of rest, reducing excess stress, staying indoors during extreme heat and humidity using fans and air conditioning. Emphasized the importance of keeping regularly scheduled MD appointments to monitor lung function and discussing techniques for breathing more efficiently throughout the day.

    ----------------------------------------------------------------------------
    Section J: Nutritional Considerations

    **POLICY FOR THIS SECTION**
    - Type of Diet (specify any special dietary requirements)
    - Issues with Swallowing/Chewing/Dentures (include any interventions or educational points)
    - Route of Nutrition if not taken orally

    Examples Related to this Section:
    1. "Member is {compliant/non-compliant} with {specific diet}. RN instructed {member/informal caregiver} on {specific diet} and {would/would not} benefit from additional dietary instruction."

    2. "Member requires diet modifications due to {specific needs or conditions}. Education provided to {member/caregiver} on cutting food into small pieces, opting for soft food, taking smaller bites, and sipping slowly."

    3. "{Member/informal caregiver} was advised to schedule a visit with the PCP for an evaluation. The member may benefit from a speech and swallow evaluation due to {specific reason}."

    4. "Trigger identified: Swallowing issues. {Member/caregiver} reports a {decline/improvement} in swallowing capabilities due to {specific cause}, such as a new diagnosis (e.g., CVA) or worsening of {specific condition}."

    5. "Member adheres to a low sodium diet. No modifications to the diet are necessary at this time. The member does not use dentures and has all teeth intact. There are no complaints of dry mouth or issues with chewing. No difficulty swallowing food has been reported."
    ----------------------------------------------------------------------------
    Section K: Medications / Allergies

    **POLICY FOR THIS SECTION**
    General Information: Document interventions (i.e., pre-pours, reminders, medication needs to be placed in member's hand or mouth due to difficulty using hands, etc.) for members who require assistance with medications, blood glucose monitoring. Document make and model of glucometer and BG ranges if the member is a diabetic and how lancets are disposed.

    - Who administers injections?
    - How are medications managed and by whom?
    - Does the member understand the indication of medication?

    Examples Related to this Section:
    Member’s {enter caregiver relationship} pre-pours medications {enter specifics}
    Example:
    1. "Daughter pre-pours every Monday and calls the member every night for reminders. The member {does/does not} remember the type/use of medication."
    2. "Document nursing intervention if the member is non-compliant with meds. The member would benefit from pharmacy prefill of medications and/or medication blister pack."
    3. "The member {is able/not able to independently} monitor blood glucose. The member’s {caregiver/aide assists} the member with blood glucose monitoring. The member uses lancets, test strips, alcohol wipes."

    "The member needs assistance opening medication bottles each time. The member takes only oral medications. The member understands the indication of each medication and is compliant with the treatment regimen."
    ----------------------------------------------------------------------------
    Section L: Treatment /Procedures

    **POLICY FOR THIS SECTION**
    General Information: Document dates for all preventive screenings/vaccinations (quality measure) or document member's refusal/reason for refusal. Also, document providers' information if available. If the exact date is not available, provide an approximate date. Describe incidents that led to ER visits or hospital stays in the last 90 days (quality measure).

    **Flu:**
    1. Ask the member if they received a Flu vaccination in the past 12 months.
    2. If refused, document teaching/advantages of receiving the flu vaccine.

    **Oxygen:**
    Document continuous or prn and diagnosis related to the need for O2.

    **Hospital/ER:**
    Document ER/hospitalization/SNF info {ER/hospital/SNF, date of admission & D/C, and diagnosis). {Reminder: Urgent Care Visits and hospitalization admissions are not considered an ER visit in UAS}.

    - Comment on preventive screenings/vaccinations (quality measure).
    - Describe incidents that led to ER visits or hospital stays in the last 90 days (quality measure).
    - Social Day/Day Health Center schedule; If a member is participating in SDC, document the reason for attending the program.
    - Dialysis Center and schedule if applicable.

    **Examples Related to this Section:**
    - **Colonoscopy:** Not recommended by PCP, or was done in the spring of 2016 (Exact day is unavailable).
    - **Dental exam:** June of 2019, or spring of 2018, winter of 2019 (Exact day is unavailable).
    - **Eye Exam:** May of 2019, or November of 2018 (Exact day is unavailable).
    - **Hearing Exam:** June of 2019, or December of 2018 (Exact day is unavailable).
    - **Influenza vaccine:** October of 2018 or within the last 12 months (Exact day is unavailable).
    - **Mammogram or Breast Exam:** June of 2019 (Exact day is unavailable).
    - **Pneumococcal vaccine:** 2 years ago, or not recommended by PCP, or within the last 5 years (Exact day is unavailable).

    **For flu shot refusal:**
    Member refused the yearly flu vaccination. RN educated {Member/informal caregiver} on the benefits of receiving the yearly flu vaccine. Instructed {Member/informal caregiver} that flu season is from October through May and the member can contact the Plan care manager to assist with getting the flu shot. Advised {Member/informal caregiver} of the nearest pharmacy location for getting a flu shot. {Member/informal caregiver} verbalized understanding and {agreed/did not agree} to receive a flu shot at this time. {Member/informal caregiver} reported that the member did receive a flu shot. Flu shot provided by {enter who provided shot} on {enter date or approximate date}.

    **Oxygen Use:**
    Member uses oxygen {@ x L/m and has oxygen supplies}.

    **Hospitalization note:**
    Member was admitted to {hospital/ER} on {admission to discharge date} at {Hospital name} for {diagnosis} and discharge instructions included {enter specifics}. {Member/informal caregiver} educated on {importance of scheduling and keeping the post-discharge appointment with PCP, medication compliance, early recognition of symptoms and to report these symptoms to MD immediately}. Provided education to {Member/informal caregiver} {use of urgent care for conditions such as respiratory infection, fever, back pain, asthma sprains, urinary problems, sprains/fractures}. Educated {Member/informal caregiver} on warning signs of {enter condition} and the importance of taking action before symptoms worsen. Identified {enter specific} as a barrier to the member seeing PCP.

    **Member's Specifics:**
    Member is up to date with all preventive screenings. Member refuses all vaccinations due to a severe allergic reaction, anaphylaxis to the flu vaccine 10 years ago. Member went to the ER last month for chest pain. Member was discharged with a diagnosis of heartburn and received new medication Omeprazole 20 mg orally once a day before meals. Member denies hospital stay in the last 90 days.
    ----------------------------------------------------------------------------
    Section M: Social Supports

    **POLICY FOR THIS SECTION**
    - Emergency Contact/Caregiver(s) information should include name, relationship, phone numbers, work/school schedule, and employer contact information. This information will be moved to the Functional Supplement section.

    **Note**: It's important to document if the member refuses to provide information or if the information is unavailable.

    Examples Related to this Section:
    - If the mutual case is with the same plan as the member, document as "Mutual is {enter name and CIN #}". If the plan is not the same as the member's, then documentation should reflect "Member lives with {enter relationship} who also receives services from {enter plan name}."

    - "Member lives with his son. Daughter Svetlana (918-637-2873) is the Power of Attorney (POA), and brother Hector (718-473-3894) is the Health Care Proxy (HCP)."
    ----------------------------------------------------------------------------
    Section N: Environmental

    **POLICY FOR THIS SECTION**
    - Documentation should detail the cleanliness and organization of the home, type of residence, and accessibility features such as stairs, elevators, ramps, or wheelchair access.

    Examples Related to this Section:
    1. "The home is clean, clutter-free, well-lit, at an appropriate temperature, with no infestations, and is safe for home care services. The member denies having limited funds and making trade-offs for financial gain."
    2. "Member's home has narrow passageways due to stacks of boxes and filled garbage bags. There are several cats; noted the smell of urine throughout the home. The living and bedroom areas are filled with clutter and present as a safety hazard for the member. The nurse assessor educated the member regarding the importance of clear passageways to prevent injury. The nurse assessor will follow up with the case manager regarding the member's safety in the home."
    --------------------------------------
"""

EXTRA = """

"""