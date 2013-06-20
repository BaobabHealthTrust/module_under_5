P.1. INITIAL NEW-BORN RECORD [program: UNDER 5 PROGRAM, scope: EXISTS]
C.1. Capture details about the birth of the child if the data does not exist in the system
Q.1.1. Place of birth [pos: 0, tt_requirenextclick: false, tt_onLoad: tt_cancel_destination += "&skip_flow=true"; __$("nextButton").style.display = "none"; skipFlow("<%= params["skip_flow"]%>"); showCategory("Initial New Born Record"); __$("category").style.fontSize = "30px"]
O.1.1.1. Home
O.1.1.2. Health facility

Q.1.2. Birth weight (grams) [pos: 1, concept: Birth weight, field_type: number, tt_pageStyleClass: NumbersWithUnknownAndDecimal, absoluteMin: 200.0, absoluteMax: 10000.0, tt_onLoad: __$("nextButton").style.display = "block"; showCategory("Initial New Born Record"); __$("category").style.fontSize = "30px"]

Q.1.3. Birth length (cm) [pos: 2, concept: Birth length, absoluteMin: 10, absoluteMax: 70, field_type: number, tt_pageStyleClass: NumbersWithUnknownAndDecimal, tt_onLoad: __$("nextButton").style.display = "block"; showCategory("Initial New Born Record"); __$("category").style.fontSize = "30px"]

Q.1.4. Head circumference [pos: 3, helpText: Head Circumference (cm), field_type: number, absoluteMin: 10, absoluteMax: 60, tt_pageStyleClass: NumbersWithUnknownAndDecimal, tt_onLoad: __$("nextButton").style.display = "block"; showCategory("Initial New Born Record"); __$("category").style.fontSize = "30px"]

Q.1.5. Observation on eyes [pos: 4, tt_requirenextclick: false, tt_onLoad: __$("nextButton").style.display = "none"; showCategory("Initial New Born Record"); __$("category").style.fontSize = "30px";]
O.1.5.1. Normal
O.1.5.2. Abnormal
O.1.5.3. Other
Q.1.5.3.1. Specify eyes abnormality [concept: Specify, pos: 5, tt_onLoad: __$("nextButton").style.display = "block"; showCategory("Initial New Born Record"); __$("category").style.fontSize = "30px"]

Q.1.6. Observation on mouth [pos: 6, tt_requirenextclick: false, tt_onLoad: __$("nextButton").style.display = "none"; showCategory("Initial New Born Record"); __$("category").style.fontSize = "30px"]
O.1.6.1. Normal
O.1.6.2. Abnormal
O.1.6.3. Other
Q.1.6.3.1. Specify mouth abnormality [concept: Specify, tt_onLoad: __$("nextButton").style.display = "block"; showCategory("Initial New Born Record"); __$("category").style.fontSize = "30px", pos: 7]

Q.1.7. Observation on umbilicus [pos: 8, tt_requirenextclick: false, tt_onLoad: __$("nextButton").style.display = "none"; showCategory("Initial New Born Record"); __$("category").style.fontSize = "30px"]
O.1.7.1. Normal
O.1.7.2. Abnormal
O.1.7.3. Other
Q.1.7.3.1. Specify umbilicus abnormality [concept: Specify, tt_onLoad: __$("nextButton").style.display = "block"; showCategory("Initial New Born Record"); __$("category").style.fontSize = "30px", pos: 9]

Q.1.8. Observation on fingers [pos: 10, tt_requirenextclick: false, tt_onLoad: __$("nextButton").style.display = "none"; showCategory("Initial New Born Record"); __$("category").style.fontSize = "30px"]
O.1.8.1. Normal
O.1.8.2. Abnormal
O.1.8.3. Other
Q.1.8.3.1. Specify fingers abnormality [concept: Specify, tt_onLoad: __$("nextButton").style.display = "block"; showCategory("Initial New Born Record"); __$("category").style.fontSize = "30px", pos: 11]

Q.1.9. Observation on toes [pos: 12, tt_requirenextclick: false, tt_onLoad: __$("nextButton").style.display = "none"; showCategory("Initial New Born Record"); __$("category").style.fontSize = "30px"]
O.1.9.1. Normal
O.1.9.2. Abnormal
O.1.9.3. Other
Q.1.9.3.1. Specify toes abnormality [concept: Specify, tt_onLoad: __$("nextButton").style.display = "block"; showCategory("Initial New Born Record"); __$("category").style.fontSize = "30px", pos: 13]

Q.1.10. Observation on feet [pos: 14, tt_requirenextclick: false, tt_onLoad: __$("nextButton").style.display = "none"; showCategory("Initial New Born Record"); __$("category").style.fontSize = "30px"]
O.1.10.1. Normal
O.1.10.2. Abnormal
O.1.10.3. Other
Q.1.10.3.1. Specify feet abnormality [concept: Specify, tt_onLoad: __$("nextButton").style.display = "block"; showCategory("Initial New Born Record"); __$("category").style.fontSize = "30px", pos: 15]

Q.1.11. Observation on spine [pos: 16, tt_requirenextclick: false, tt_onLoad: __$("nextButton").style.display = "none"; showCategory("Initial New Born Record"); __$("category").style.fontSize = "30px"]
O.1.11.1. Normal
O.1.11.2. Abnormal
O.1.11.3. Other
Q.1.11.3.1. Specify spine abnormality [concept: Specify, tt_onLoad: __$("nextButton").style.display = "block"; showCategory("Initial New Born Record"); __$("category").style.fontSize = "30px", pos: 17]

Q.1.12. Observation on genitalia [pos: 18, tt_requirenextclick: false, tt_onLoad: __$("nextButton").style.display = "none"; showCategory("Initial New Born Record"); __$("category").style.fontSize = "30px"]
O.1.12.1. Normal
O.1.12.2. Abnormal
O.1.12.3. Other
Q.1.12.3.1. Specify genitalia abnormality [concept: Specify, tt_onLoad: __$("nextButton").style.display = "block"; showCategory("Initial New Born Record"); __$("category").style.fontSize = "30px", pos: 19]

Q.1.13. Observation on rectum [pos: 20, tt_requirenextclick: false, tt_onLoad: __$("nextButton").style.display = "none"; showCategory("Initial New Born Record"); __$("category").style.fontSize = "30px"]
O.1.13.1. Normal
O.1.13.2. Abnormal
O.1.13.3. Other
Q.1.13.3.1. Specify rectum abnormality [concept: Specify, tt_onLoad: __$("nextButton").style.display = "block"; showCategory("Initial New Born Record"); __$("category").style.fontSize = "30px", pos: 21]

Q.1.14. Observation on suckling reflex [pos: 22, tt_onLoad: __$("nextButton").style.display = "block"; __$("nextButton").innerHTML = "<span>Finish</span>"; showCategory("Initial New Born Record"); __$("category").style.fontSize = "30px"]
O.1.14.1. Normal
O.1.14.2. Abnormal
O.1.14.3. Other
Q.1.14.3.1. Specify suckling reflex abnormality [concept: Specify, pos: 23, tt_onLoad: showCategory("Initial New Born Record"); __$("category").style.fontSize = "30px"]



