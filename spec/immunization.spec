P.1. IMMUNIZATION RECORD [program: UNDER 5 PROGRAM]
C.1. Record immunization of baby
Q.1.1. BCG immunization was given at birth?
O.1.1.1. No
O.1.1.2. Yes
Q.1.1.2.1. Immunization year
O.1.1.2.1.1. Unknown

Q.1.1.2.2. Immunization month [condition: __$("1.1.2.1").value.trim() != "Unknown"]
O.1.1.2.2.1. January
O.1.1.2.2.2. February
O.1.1.2.2.3. March
O.1.1.2.2.4. April
O.1.1.2.2.5. May
O.1.1.2.2.6. June
O.1.1.2.2.7. July
O.1.1.2.2.8. August
O.1.1.2.2.9. September
O.1.1.2.2.10. October
O.1.1.2.2.11. November
O.1.1.2.2.12. December
O.1.1.2.2.13. Unknown

Q.1.1.2.3. Immunization day [condition: __$("1.1.2.2").value.trim() != "Unknown"]

Q.1.1.2.4. Has immunization scar been seen?
O.1.1.2.4.1. Yes
O.1.1.2.4.2. No
Q.1.1.2.4.2.1. Repeat BCG immunization given? [condition: var d = checkBCGDate(); d > 12;] 
O.1.1.2.4.2.1.1. No
O.1.1.2.4.2.1.2. Yes
Q.1.1.2.4.2.1.2.1. Repeat immunization dose date [field_type: date]

Q.1.2. Was DPT-HepB-Hib 1 vaccine given at 6 weeks or later? [condition: <%= @patient.age_in_months > 1.5 and !@patient.dpt1.downcase == "yes" %>]
O.1.2.1. No
O.1.2.2. Yes
Q.1.2.2.1. Date DPT-HepB-Hib 1 vaccine given [field_type: date]

Q.1.3. Was DPT-HepB-Hib 2 vaccine given at 1 month after first dose? [condition: <%= @patient.age_in_months > 2 and !@patient.dpt2.downcase == "yes" %>]
O.1.3.1. No
O.1.3.2. Yes
Q.1.3.2.1. Date DPT-HepB-Hib 2 vaccine given [field_type: date] 

Q.1.4. Was DPT-HepB-Hib 3 vaccine given at 1 month after second dose? [condition: <%= @patient.age_in_months > 2 and !@patient.dpt3.downcase == "yes" %>]
O.1.4.1. No
O.1.4.2. Yes
Q.1.4.2.1. Date DPT-HepB-Hib 3 vaccine given [field_type: date]

Q.1.5. PCV 1 vaccine given at 6 weeks or later? [condition: <%= @patient.age_in_months > 1.5 and !@patient.pcv1.downcase == "yes" %>] 
O.1.5.1. No
O.1.5.2. Yes
Q.1.5.2.1. Date PCV 1 vaccine given [field_type: date]

Q.1.6. PCV 2 vaccine given at 1 month after first dose? [condition: <%= @patient.age_in_months > 1.5 and !@patient.pcv2.downcase == "yes" %>] 
O.1.6.1. No
O.1.6.2. Yes
Q.1.6.2.1. Date PCV 2 vaccine given [field_type: date]

Q.1.7. PCV 3 vaccine given at 1 month after second dose? [condition: <%= @patient.age_in_months >= 1.5 and !@patient.pcv3.downcase == "yes" %>] 
O.1.7.1. No
O.1.7.2. Yes
Q.1.7.2.1. Date PCV 31 vaccine given [field_type: date]

Q.1.8. First polio vaccine at birth [condition: <%= @patient.age_in_months < 0.5 and !@patient.polio0.downcase == "yes" %>] 
O.1.8.1. No
O.1.8.2. Yes
Q.1.8.2.1. Date first Polio vaccine given [field_type: date]

Q.1.9. Second polio vaccine at 1.5 months [condition: <%= @patient.age_in_months >= 1.5 and !@patient.polio1.downcase == "yes" %>]  
O.1.9.1. No
O.1.9.2. Yes
Q.1.9.2.1. Date second Polio vaccine given [field_type: date]

Q.1.10. Third polio vaccine at 2.5 months [condition: <%= @patient.age_in_months >= 2.5 and !@patient.polio2.downcase == "yes" %>]  
O.1.10.1. No
O.1.10.2. Yes
Q.1.10.2.1. Date third Polio vaccine given [field_type: date] 

Q.1.11. Fourth polio vaccine at 3.5 months [condition: <%= @patient.age_in_months >= 3.5 and !@patient.polio3.downcase == "yes" %>]  
O.1.11.1. No
O.1.11.2. Yes
Q.1.11.2.1. Date fourth Polio vaccine given [field_type: date] 

Q.1.12. Measles vaccine at 9 months 
O.1.12.1. No
O.1.12.2. Yes
Q.1.12.2.1. Date measles vaccine given

Q.1.13. Mother HIV Status
O.1.13.1. Negative
O.1.13.2. Positive
Q.1.13.2.1. Childs current HIV status
O.1.13.2.1.1. HIV infected
O.1.13.2.1.2. Not HIV infected
O.1.13.2.1.3. Not confirmed diagnosis




