P.1. UNDER 5 VISIT [program: UNDER 5 PROGRAM, concept: Weight, scope: TODAY]
C.1. On each regular child under 5 visit, capture the following details:

Q.1.1.3. Diagnosis (Optional) [name: concept[Diagnosis][], ajaxUrl: /encounters/diagnoses?search=, pos: 1, allowFreeText: true, tt_onLoad: __$("nextButton").style.display = "block"; showCategory("Under 5 Visit"); __$("category").style.fontSize = "30px", optional: true]

Q.1.1.4. Next Diagnosis [name: concept[Diagnosis][], tt_onLoad: showCategory("Under 5 Visit"); __$("category").style.fontSize = "30px", condition: __$("1.1.3").value.trim().length > 0, ajaxUrl: /encounters/diagnoses?search=, optional: true, pos: 2]

Q.1.1.5. Next Diagnosis [name: concept[Diagnosis][], tt_onLoad: showCategory("Under 5 Visit"); __$("category").style.fontSize = "30px", condition: __$("1.1.4").value.trim().length > 0, ajaxUrl: /encounters/diagnoses?search=, optional: true, pos: 3]

Q.1.1.6. Next Diagnosis [name: concept[Diagnosis][], tt_onLoad: showCategory("Under 5 Visit"); __$("category").style.fontSize = "30px", condition: __$("1.1.5").value.trim().length > 0, ajaxUrl: /encounters/diagnoses?search=, optional: true, pos: 4]

Q.1.4. Height (cm) [pos: 32, min: 20, max: 130, tt_pageStyleClass: NumbersWithUnknownAndDecimal, tt_onLoad: showCategory("Under 5 Visit"); __$("category").style.fontSize = "30px", field_type: number]

Q.1.5. Weight (grams) [pos: 33, concept: Weight, tt_onLoad: showCategory("Under 5 Visit"); __$("category").style.fontSize = "30px", min: 2500, max: 34000, tt_pageStyleClass: NumbersOnly, field_type: number]

Q.1.6. Notes [pos: 34, tt_onLoad: showCategory("Under 5 Visit"); __$("category").style.fontSize = "30px", field_type: textarea, optional: true]








