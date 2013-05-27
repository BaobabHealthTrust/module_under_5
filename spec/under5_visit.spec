P.1. UNDER 5 VISIT [program: UNDER 5 PROGRAM, includejs: dispense;generics, includecss: dispense;drug-style]
C.1. On each regular child under 5 visit, capture the following details:
Q.1.1. Are there any diagnoses to be captured? [pos: 0, disabled: disabled, tt_requirenextclick: false, tt_onLoad: tt_cancel_destination += "&skip_flow=true"; __$("nextButton").style.display = "none"; skipFlow("<%= params["skip_flow"]%>"); showCategory("Under 5 Visit"); __$("category").style.fontSize = "30px";]
O.1.1.1. No
O.1.1.2. Yes

Q.1.1.3. Diagnosis [name: concept[Diagnosis][], condition: __$("1.1").value.trim() == "Yes", ajaxUrl: /encounters/diagnoses?search=, pos: 1, tt_onLoad: __$("nextButton").style.display = "block"; showCategory("Under 5 Visit"); __$("category").style.fontSize = "30px";]

Q.1.1.4. Diagnosis [name: concept[Diagnosis][], tt_onLoad: showCategory("Under 5 Visit"); __$("category").style.fontSize = "30px", condition: __$("1.1").value.trim() == "Yes" && __$("1.1.3").value.trim().length > 0, ajaxUrl: /encounters/diagnoses?search=, optional: true, pos: 2]

Q.1.1.5. Diagnosis [name: concept[Diagnosis][], tt_onLoad: showCategory("Under 5 Visit"); __$("category").style.fontSize = "30px", condition: __$("1.1").value.trim() == "Yes" && __$("1.1.4").value.trim().length > 0, ajaxUrl: /encounters/diagnoses?search=, optional: true, pos: 3]

Q.1.1.6. Diagnosis [name: concept[Diagnosis][], tt_onLoad: showCategory("Under 5 Visit"); __$("category").style.fontSize = "30px", condition: __$("1.1").value.trim() == "Yes" && __$("1.1.5").value.trim().length > 0, ajaxUrl: /encounters/diagnoses?search=, optional: true, pos: 4]

Q.1.1.7. Diagnosis [name: concept[Diagnosis][], tt_onLoad: showCategory("Under 5 Visit"); __$("category").style.fontSize = "30px", condition: __$("1.1").value.trim() == "Yes" && __$("1.1.6").value.trim().length > 0, ajaxUrl: /encounters/diagnoses?search=, optional: true, pos: 5]

Q.1.1.8. Diagnosis [name: concept[Diagnosis][], tt_onLoad: showCategory("Under 5 Visit"); __$("category").style.fontSize = "30px", condition: __$("1.1").value.trim() == "Yes" && __$("1.1.7").value.trim().length > 0, ajaxUrl: /encounters/diagnoses?search=, optional: true, pos: 6]

Q.1.1.9. Diagnosis [name: concept[Diagnosis][], tt_onLoad: showCategory("Under 5 Visit"); __$("category").style.fontSize = "30px", condition: __$("1.1").value.trim() == "Yes" && __$("1.1.8").value.trim().length > 0, ajaxUrl: /encounters/diagnoses?search=, optional: true, pos: 7]

Q.1.1.10. Diagnosis [name: concept[Diagnosis][], tt_onLoad: showCategory("Under 5 Visit"); __$("category").style.fontSize = "30px", condition: __$("1.1").value.trim() == "Yes" && __$("1.1.9").value.trim().length > 0, ajaxUrl: /encounters/diagnoses?search=, optional: true, pos: 8]

Q.1.1.11. Diagnosis [name: concept[Diagnosis][], tt_onLoad: showCategory("Under 5 Visit"); __$("category").style.fontSize = "30px", condition: __$("1.1").value.trim() == "Yes" && __$("1.1.10").value.trim().length > 0, ajaxUrl: /encounters/diagnoses?search=, optional: true, pos: 9]

Q.1.1.12. Diagnosis [name: concept[Diagnosis][], tt_onLoad: showCategory("Under 5 Visit"); __$("category").style.fontSize = "30px", condition: __$("1.1").value.trim() == "Yes" && __$("1.1.11").value.trim().length > 0, ajaxUrl: /encounters/diagnoses?search=, optional: true, pos: 10, tt_onLoad: __$("nextButton").style.display = "block"]

Q.1.2. Are there any lab results to be captured? [disabled: disabled, pos: 11, tt_requirenextclick: false, tt_onLoad: __$("nextButton").style.display = "none"; showCategory("Under 5 Visit"); __$("category").style.fontSize = "30px"]
O.1.2.1. No
O.1.2.2. Yes

Q.1.2.2.1. 1<sup>st</sup> Lab test done [name: concept[Lab test done][], condition: __$("1.2").value.trim() == "Yes", pos: 12, tt_onLoad: __$("nextButton").style.display = "block"; showCategory("Under 5 Visit"); __$("category").style.fontSize = "30px"]

Q.1.2.2.2. 1<sup>st</sup> Lab test result [name: concept[Lab test result][], tt_onLoad: showCategory("Under 5 Visit"); __$("category").style.fontSize = "30px", condition: __$("1.2.2.1").value.trim().length > 0, pos: 13]

Q.1.2.2.3. 2<sup>nd</sup> Lab test done [name: concept[Lab test done][],tt_onLoad: showCategory("Under 5 Visit"); __$("category").style.fontSize = "30px",  condition: __$("1.2").value.trim() == "Yes" && __$("1.2.2.1").value.trim().length > 0, pos: 14, optional: true]

Q.1.2.2.4. 2<sup>nd</sup> Lab test result [name: concept[Lab test result][], tt_onLoad: showCategory("Under 5 Visit"); __$("category").style.fontSize = "30px", condition: __$("1.2.2.3").value.trim().length > 0, pos: 15]

Q.1.2.2.5. 3<sup>rd</sup> Lab test done [name: concept[Lab test done][], tt_onLoad: showCategory("Under 5 Visit"); __$("category").style.fontSize = "30px", condition: __$("1.2").value.trim() == "Yes" && __$("1.2.2.3").value.trim().length > 0, pos: 16, optional: true]

Q.1.2.2.6. 3<sup>rd</sup> Lab test result [name: concept[Lab test result][], tt_onLoad: showCategory("Under 5 Visit"); __$("category").style.fontSize = "30px", condition: __$("1.2.2.5").value.trim().length > 0, pos: 17]

Q.1.2.2.7. 4<sup>th</sup> Lab test done [name: concept[Lab test done][], tt_onLoad: showCategory("Under 5 Visit"); __$("category").style.fontSize = "30px", condition: __$("1.2").value.trim() == "Yes" && __$("1.2.2.5").value.trim().length > 0, pos: 18, optional: true]

Q.1.2.2.8. 4<sup>th</sup> Lab test result [name: concept[Lab test result][], tt_onLoad: showCategory("Under 5 Visit"); __$("category").style.fontSize = "30px", condition: __$("1.2.2.7").value.trim().length > 0, pos: 19]

Q.1.2.2.9. 5<sup>th</sup> Lab test done [name: concept[Lab test done][], tt_onLoad: showCategory("Under 5 Visit"); __$("category").style.fontSize = "30px", condition: __$("1.2").value.trim() == "Yes" && __$("1.2.2.7").value.trim().length > 0, pos: 20, optional: true]

Q.1.2.2.10. 5<sup>th</sup> Lab test result [name: concept[Lab test result][], tt_onLoad: showCategory("Under 5 Visit"); __$("category").style.fontSize = "30px", condition: __$("1.2.2.9").value.trim().length > 0]

Q.1.2.2.11. 6<sup>th</sup> Lab test done [name: concept[Lab test done][], tt_onLoad: showCategory("Under 5 Visit"); __$("category").style.fontSize = "30px", condition: __$("1.2").value.trim() == "Yes" && __$("1.2.2.9").value.trim().length > 0, pos: 21, optional: true]

Q.1.2.2.12. 6<sup>th</sup> Lab test result [name: concept[Lab test result][], tt_onLoad: showCategory("Under 5 Visit"); __$("category").style.fontSize = "30px", condition: __$("1.2.2.11").value.trim().length > 0, pos: 22]

Q.1.2.2.13. 7<sup>th</sup> Lab test done [name: concept[Lab test done][], tt_onLoad: showCategory("Under 5 Visit"); __$("category").style.fontSize = "30px", condition: __$("1.2").value.trim() == "Yes" && __$("1.2.2.11").value.trim().length > 0, pos: 23, optional: true]

Q.1.2.2.14. 7<sup>th</sup> Lab test result [name: concept[Lab test result][], tt_onLoad: showCategory("Under 5 Visit"); __$("category").style.fontSize = "30px", condition: __$("1.2.2.13").value.trim().length > 0, pos: 24]

Q.1.2.2.15. 8<sup>th</sup> Lab test done [name: concept[Lab test done][], tt_onLoad: showCategory("Under 5 Visit"); __$("category").style.fontSize = "30px", condition: __$("1.2").value.trim() == "Yes" && __$("1.2.2.13").value.trim().length > 0, pos: 25, optional: true]

Q.1.2.2.16. 8<sup>th</sup> Lab test result [name: concept[Lab test result][], condition: __$("1.2.2.15").value.trim().length > 0, pos: 26]

Q.1.2.2.17. 9<sup>th</sup> Lab test done [name: concept[Lab test done][], tt_onLoad: showCategory("Under 5 Visit"); __$("category").style.fontSize = "30px", condition: __$("1.2").value.trim() == "Yes" && __$("1.2.2.15").value.trim().length > 0, pos: 27, optional: true]

Q.1.2.2.18. 9<sup>th</sup> Lab test result [name: concept[Lab test result][], tt_onLoad: showCategory("Under 5 Visit"); __$("category").style.fontSize = "30px", condition: __$("1.2.2.17").value.trim().length > 0, pos: 28]

Q.1.2.2.19. 10<sup>th</sup> Lab test done [name: concept[Lab test done][], tt_onLoad: showCategory("Under 5 Visit"); __$("category").style.fontSize = "30px", condition: __$("1.2").value.trim() == "Yes" && __$("1.2.2.17").value.trim().length > 0, pos: 29, optional: true]

Q.1.2.2.20. 10<sup>th</sup> Lab test result [name: concept[Lab test result][], tt_onLoad: showCategory("Under 5 Visit"); __$("category").style.fontSize = "30px", condition: __$("1.2.2.19").value.trim().length > 0, pos: 30]

Q.1.3. Treatment [tt_onLoad: generateGenerics(<%= @patient.id %>); showCategory("Under 5 Visit"); __$("category").style.fontSize = "30px"; __$("nextButton").style.display = "block", tt_onUnLoad: removeGenerics(), tt_pageStyleClass: NoControls, optional: true, pos: 31]

Q.1.4. Height (cm) [pos: 32, tt_pageStyleClass: NumbersWithUnknownAndDecimal, tt_onLoad: showCategory("Under 5 Visit"); __$("category").style.fontSize = "30px", field_type: number]

Q.1.5. Weight (Grams) [pos: 33, tt_onLoad: showCategory("Under 5 Visit"); __$("category").style.fontSize = "30px", validationRule: ^\d+\.\d+$|^Unknown$, validationMessage: Not a valid weight, tt_pageStyleClass: NumbersWithUnknownAndDecimal, field_type: number]

Q.1.6. Notes [pos: 34, tt_onLoad: showCategory("Under 5 Visit"); __$("category").style.fontSize = "30px", field_type: textarea, optional: true]








