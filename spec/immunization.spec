P.1. IMMUNIZATION RECORD [program: UNDER 5 PROGRAM, scope: RECENT, concept: Mother HIV Status]
C.1. Record immunization of baby
Q.1.1. BCG immunization was given at birth? [pos: 0, tt_onLoad: tt_cancel_destination += "&skip_flow=true";  skipFlow("<%= params["skip_flow"]%>"); showCategory("Immunization Record"); __$("category").style.fontSize = "30px"]
O.1.1.1. No
O.1.1.2. Yes
Q.1.1.2.1. Immunization day [pos: 1, helpText: Immunization Date, field_type: date, tt_onUnLoad: showCategory("Immunization Record"); __$("category").style.fontSize = "30px", absoluteMin: <%= @patient.person.birthdate.to_date %>, absoluteMax: <%= (session["datetime"].to_date rescue  Date.today) %>]

Q.1.1.2.4. Has immunization scar been seen? [tt_onUnLoad: showCategory("Immunization Record"); __$("category").style.fontSize = "30px", pos: 4]
O.1.1.2.4.1. Yes
O.1.1.2.4.2. No
Q.1.1.2.4.2.1. Repeat BCG immunization given? [tt_onUnLoad: showCategory("Immunization Record"); __$("category").style.fontSize = "30px", pos: 5, condition: var d = checkBCGDate("<%= session["datetime"].to_date rescue Date.today%>"); d > 12;]
O.1.1.2.4.2.1.1. No
O.1.1.2.4.2.1.2. Yes
Q.1.1.2.4.2.1.2.1. Repeat immunization dose date [tt_onUnLoad: showCategory("Immunization Record"); __$("category").style.fontSize = "30px", field_type: date, pos: 6]

Q.1.2. Was DPT-HepB-Hib 1 vaccine given at 6 weeks or later? [pos: 7, tt_onUnLoad: showCategory("Immunization Record"); __$("category").style.fontSize = "30px", condition: <%= @patient.age_in_months > 1.5 and @patient.dpt1.downcase.strip != "yes" %>]
O.1.2.1. No
O.1.2.2. Yes
Q.1.2.2.1. Date DPT-HepB-Hib 1 vaccine given [tt_onUnLoad: showCategory("Immunization Record"); __$("category").style.fontSize = "30px", field_type: date, pos: 8]

Q.1.3. Was DPT-HepB-Hib 2 vaccine given at 1 month after first dose? [pos: 9, tt_onUnLoad: showCategory("Immunization Record"); __$("category").style.fontSize = "30px", condition: <%= @patient.age_in_months > 2 and @patient.dpt2.downcase.strip != "yes" %>]
O.1.3.1. No
O.1.3.2. Yes
Q.1.3.2.1. Date DPT-HepB-Hib 2 vaccine given [tt_onUnLoad: showCategory("Immunization Record"); __$("category").style.fontSize = "30px", field_type: date, pos: 10]

Q.1.4. Was DPT-HepB-Hib 3 vaccine given at 1 month after second dose? [pos: 11, tt_onUnLoad: showCategory("Immunization Record"); __$("category").style.fontSize = "30px", condition: <%= @patient.age_in_months > 2 and @patient.dpt3.downcase.strip != "yes" %>]
O.1.4.1. No
O.1.4.2. Yes
Q.1.4.2.1. Date DPT-HepB-Hib 3 vaccine given [field_type: date, pos: 12, tt_onUnLoad: showCategory("Immunization Record"); __$("category").style.fontSize = "30px",]

Q.1.5. PCV 1 vaccine given at 6 weeks or later? [tt_onUnLoad: showCategory("Immunization Record"); __$("category").style.fontSize = "30px", pos: 13, condition: <%= @patient.age_in_months > 1.5 and @patient.pcv1.downcase.strip != "yes" %>]
O.1.5.1. No
O.1.5.2. Yes
Q.1.5.2.1. Date PCV 1 vaccine given [tt_onUnLoad: showCategory("Immunization Record"); __$("category").style.fontSize = "30px", field_type: date, pos: 14]

Q.1.6. PCV 2 vaccine given at 1 month after first dose? [tt_onUnLoad: showCategory("Immunization Record"); __$("category").style.fontSize = "30px", pos: 15, condition: <%= @patient.age_in_months > 1.5 and @patient.pcv2.downcase.strip != "yes" %>]
O.1.6.1. No
O.1.6.2. Yes
Q.1.6.2.1. Date PCV 2 vaccine given [tt_onUnLoad: showCategory("Immunization Record"); __$("category").style.fontSize = "30px", field_type: date, pos: 16]

Q.1.7. PCV 3 vaccine given at 1 month after second dose? [tt_onUnLoad: showCategory("Immunization Record"); __$("category").style.fontSize = "30px", pos: 17, condition: <%= @patient.age_in_months >= 1.5 and @patient.pcv3.downcase != "yes" %>]
O.1.7.1. No
O.1.7.2. Yes
Q.1.7.2.1. Date PCV 31 vaccine given [tt_onUnLoad: showCategory("Immunization Record"); __$("category").style.fontSize = "30px", field_type: date, pos: 18]

Q.1.8. First polio vaccine at birth [tt_onUnLoad: showCategory("Immunization Record"); __$("category").style.fontSize = "30px", pos: 19, condition: <%= @patient.age_in_months < 0.5 and @patient.polio0.downcase != "yes" %>]
O.1.8.1. No
O.1.8.2. Yes
Q.1.8.2.1. Date first Polio vaccine given [tt_onUnLoad: showCategory("Immunization Record"); __$("category").style.fontSize = "30px", field_type: date, pos: 20]

Q.1.9. Second polio vaccine at 1.5 months [tt_onUnLoad: showCategory("Immunization Record"); __$("category").style.fontSize = "30px", pos: 21, condition: <%= @patient.age_in_months >= 1.5 and @patient.polio1.downcase != "yes" %>]
O.1.9.1. No
O.1.9.2. Yes
Q.1.9.2.1. Date second Polio vaccine given [tt_onUnLoad: showCategory("Immunization Record"); __$("category").style.fontSize = "30px", field_type: date, pos: 22]

Q.1.10. Third polio vaccine at 2.5 months [tt_onUnLoad: showCategory("Immunization Record"); __$("category").style.fontSize = "30px", pos: 23, condition: <%= @patient.age_in_months >= 2.5 and @patient.polio2.downcase != "yes" %>]
O.1.10.1. No
O.1.10.2. Yes
Q.1.10.2.1. Date third Polio vaccine given [tt_onUnLoad: showCategory("Immunization Record"); __$("category").style.fontSize = "30px", field_type: date, pos: 24]

Q.1.11. Fourth polio vaccine at 3.5 months [tt_onUnLoad: showCategory("Immunization Record"); __$("category").style.fontSize = "30px", pos: 25, condition: <%= @patient.age_in_months >= 3.5 and @patient.polio3.downcase != "yes" %>]
O.1.11.1. No
O.1.11.2. Yes
Q.1.11.2.1. Date fourth Polio vaccine given [tt_onUnLoad: showCategory("Immunization Record"); __$("category").style.fontSize = "30px", field_type: date, pos: 26]

Q.1.12. Measles vaccine at 9 months [tt_onUnLoad: showCategory("Immunization Record"); __$("category").style.fontSize = "30px", pos: 27]
O.1.12.1. No
O.1.12.2. Yes
Q.1.12.2.1. Date measles vaccine given [tt_onUnLoad: showCategory("Immunization Record"); __$("category").style.fontSize = "30px", pos: 28, field_type: date]

Q.1.13. Mother HIV Status [tt_onUnLoad: showCategory("Immunization Record"); __$("category").style.fontSize = "30px", pos: 29]
O.1.13.1. Negative
O.1.13.2. Positive
Q.1.13.2.1. Child current HIV status [concept: HIV Status, tt_onUnLoad: showCategory("Immunization Record"); __$("category").style.fontSize = "30px", pos: 30]
O.1.13.2.1.1. HIV infected
O.1.13.2.1.2. Not HIV infected
O.1.13.2.1.3. Not confirmed diagnosis
