P.1. SURGICAL HISTORY [program: UNDER 5 PROGRAM]
Q.1.1. Ever had any surgical procedure?
O.1.1.1. No
O.1.1.2. Yes

Q.1.1.3. Diagnosis [condition: __$("1.1").value.trim() == "Yes"]
Q.1.1.4. Diagnosis date [condition: __$("1.1").value.trim() == "Yes", field_type: date]

Q.1.1.5. Diagnosis [condition: __$("1.1").value.trim() == "Yes" && __$("1.1.3").value.trim().length > 0, optional: true]
Q.1.1.6. Diagnosis date [condition: __$("1.1").value.trim() == "Yes" && __$("1.1.5").value.trim().length > 0, field_type: date]

Q.1.1.7. Diagnosis [condition: __$("1.1").value.trim() == "Yes" && __$("1.1.5").value.trim().length > 0, optional: true]
Q.1.1.8. Diagnosis date [condition: __$("1.1").value.trim() == "Yes" && __$("1.1.7").value.trim().length > 0, field_type: date]

Q.1.1.9. Diagnosis [condition: __$("1.1").value.trim() == "Yes" && __$("1.1.7").value.trim().length > 0, optional: true]
Q.1.1.10. Diagnosis date [condition: __$("1.1").value.trim() == "Yes" && __$("1.1.9").value.trim().length > 0, field_type: date]

Q.1.1.11. Diagnosis [condition: __$("1.1").value.trim() == "Yes" && __$("1.1.9").value.trim().length > 0, optional: true]
Q.1.1.12. Diagnosis date [condition: __$("1.1").value.trim() == "Yes" && __$("1.1.11").value.trim().length > 0, field_type: date]

