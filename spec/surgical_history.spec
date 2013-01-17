P.1. SURGICAL HISTORY [program: UNDER 5 PROGRAM]
Q.1.1. Ever had any surgical procedure? [pos: 0]
O.1.1.1. No
O.1.1.2. Yes

Q.1.1.3. Diagnosis [name: concept[Diagnosis][], condition: __$("1.1").value.trim() == "Yes", pos: 1]
Q.1.1.4. Diagnosis date [name: concept[Diagnosis date][], condition: __$("1.1").value.trim() == "Yes", field_type: date, pos: 2]

Q.1.1.5. Diagnosis [name: concept[Diagnosis][], condition: __$("1.1").value.trim() == "Yes" && __$("1.1.3").value.trim().length > 0, optional: true, pos: 3]
Q.1.1.6. Diagnosis date [name: concept[Diagnosis date][], condition: __$("1.1").value.trim() == "Yes" && __$("1.1.5").value.trim().length > 0, field_type: date, pos: 4]

Q.1.1.7. Diagnosis [name: concept[Diagnosis][], condition: __$("1.1").value.trim() == "Yes" && __$("1.1.5").value.trim().length > 0, optional: true, pos: 5]
Q.1.1.8. Diagnosis date [name: concept[Diagnosis date][], condition: __$("1.1").value.trim() == "Yes" && __$("1.1.7").value.trim().length > 0, field_type: date, pos: 6]

Q.1.1.9. Diagnosis [name: concept[Diagnosis][], condition: __$("1.1").value.trim() == "Yes" && __$("1.1.7").value.trim().length > 0, optional: true, pos: 7]
Q.1.1.10. Diagnosis date [name: concept[Diagnosis date][], condition: __$("1.1").value.trim() == "Yes" && __$("1.1.9").value.trim().length > 0, field_type: date, pos: 8]

Q.1.1.11. Diagnosis [name: concept[Diagnosis][], condition: __$("1.1").value.trim() == "Yes" && __$("1.1.9").value.trim().length > 0, optional: true, pos: 9]
Q.1.1.12. Diagnosis date [name: concept[Diagnosis date][], condition: __$("1.1").value.trim() == "Yes" && __$("1.1.11").value.trim().length > 0, field_type: date, pos: 10]

