P.1. UNDER 5 VISIT [program: UNDER 5 PROGRAM]
C.1. On each regular child under 5 visit, capture the following details:
Q.1.1. Are there any diagnoses to be captured? [disabled: disabled]
O.1.1.1. No
O.1.1.2. Yes

Q.1.1.3. Diagnosis [condition: __$("1.1").value.trim() == "Yes", ajaxUrl: /encounters/diagnoses]

Q.1.1.4. Diagnosis [condition: __$("1.1").value.trim() == "Yes" && __$("1.1.3").value.trim().length > 0, ajaxUrl: /encounters/diagnoses, optional: true]

Q.1.1.5. Diagnosis [condition: __$("1.1").value.trim() == "Yes" && __$("1.1.4").value.trim().length > 0, ajaxUrl: /encounters/diagnoses, optional: true]

Q.1.1.6. Diagnosis [condition: __$("1.1").value.trim() == "Yes" && __$("1.1.5").value.trim().length > 0, ajaxUrl: /encounters/diagnoses, optional: true]

Q.1.1.7. Diagnosis [condition: __$("1.1").value.trim() == "Yes" && __$("1.1.6").value.trim().length > 0, ajaxUrl: /encounters/diagnoses, optional: true]

Q.1.1.8. Diagnosis [condition: __$("1.1").value.trim() == "Yes" && __$("1.1.7").value.trim().length > 0, ajaxUrl: /encounters/diagnoses, optional: true]

Q.1.1.9. Diagnosis [condition: __$("1.1").value.trim() == "Yes" && __$("1.1.8").value.trim().length > 0, ajaxUrl: /encounters/diagnoses, optional: true]

Q.1.1.10. Diagnosis [condition: __$("1.1").value.trim() == "Yes" && __$("1.1.9").value.trim().length > 0, ajaxUrl: /encounters/diagnoses, optional: true]

Q.1.1.11. Diagnosis [condition: __$("1.1").value.trim() == "Yes" && __$("1.1.10").value.trim().length > 0, ajaxUrl: /encounters/diagnoses, optional: true]

Q.1.1.12. Diagnosis [condition: __$("1.1").value.trim() == "Yes" && __$("1.1.11").value.trim().length > 0, ajaxUrl: /encounters/diagnoses, optional: true]

Q.1.2. Are there any lab results to be captured? [disabled: disabled]
O.1.2.1. No
O.1.2.2. Yes

Q.1.2.2.1. Lab test done [condition: __$("1.2").value.trim() == "Yes"]

Q.1.2.2.2. Lab test result [condition: __$("1.2.2.1").value.trim().length > 0]

Q.1.2.2.3. Lab test done [condition: __$("1.2").value.trim() == "Yes" && __$("1.2.2.1").value.trim().length > 0]

Q.1.2.2.4. Lab test result [condition: __$("1.2.2.3").value.trim().length > 0]

Q.1.2.2.5. Lab test done [condition: __$("1.2").value.trim() == "Yes" && __$("1.2.2.3").value.trim().length > 0]

Q.1.2.2.6. Lab test result [condition: __$("1.2.2.5").value.trim().length > 0]

Q.1.2.2.7. Lab test done [condition: __$("1.2").value.trim() == "Yes" && __$("1.2.2.5").value.trim().length > 0]

Q.1.2.2.8. Lab test result [condition: __$("1.2.2.7").value.trim().length > 0]

Q.1.2.2.9. Lab test done [condition: __$("1.2").value.trim() == "Yes" && __$("1.2.2.7").value.trim().length > 0]

Q.1.2.2.10. Lab test result [condition: __$("1.2.2.9").value.trim().length > 0]

Q.1.2.2.11. Lab test done [condition: __$("1.2").value.trim() == "Yes" && __$("1.2.2.9").value.trim().length > 0]

Q.1.2.2.12. Lab test result [condition: __$("1.2.2.11").value.trim().length > 0]

Q.1.2.2.13. Lab test done [condition: __$("1.2").value.trim() == "Yes" && __$("1.2.2.11").value.trim().length > 0]

Q.1.2.2.14. Lab test result [condition: __$("1.2.2.13").value.trim().length > 0]

Q.1.2.2.15. Lab test done [condition: __$("1.2").value.trim() == "Yes" && __$("1.2.2.13").value.trim().length > 0]

Q.1.2.2.16. Lab test result [condition: __$("1.2.2.15").value.trim().length > 0]

Q.1.2.2.17. Lab test done [condition: __$("1.2").value.trim() == "Yes" && __$("1.2.2.15").value.trim().length > 0]

Q.1.2.2.18. Lab test result [condition: __$("1.2.2.17").value.trim().length > 0]

Q.1.2.2.19. Lab test done [condition: __$("1.2").value.trim() == "Yes" && __$("1.2.2.17").value.trim().length > 0]

Q.1.2.2.20. Lab test result [condition: __$("1.2.2.19").value.trim().length > 0]

Q.1.3. Treatment [tt_onLoad: generateGenerics(<%= @patient.id %>), tt_onUnLoad: removeGenerics(), tt_pageStyleClass: NoControls, optional: true]

Q.1.4. Height

Q.1.5. Weight

Q.1.6. Notes







