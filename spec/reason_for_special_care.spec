P.1. Reason for special care [program: UNDER 5 PROGRAM, scope: RECENT, concept: Weight less than 2500g]
C.1. Check if child needs special care
Q.1.1. Weight less than 2500g [helpText: Child was born underweight?, pos: 0, tt_requirenextclick: false, tt_onLoad: try{$("touchscreenInput" + tstCurrentPage).value = "<%= @patient.low_birth_weight? rescue nil%>"}catch(c){}; tt_cancel_destination += "&skip_flow=true"; __$("nextButton").style.display = "none"; skipFlow("<%= params["skip_flow"]%>"); showCategory("Reason For Special Care"); __$("category").style.fontSize = "30px"]
O.1.1.1. Yes
O.1.1.2. No

Q.1.2. Baby born less than 2 years since last birth of other child [helpText: Child was born less than 2 years since last birth? ,pos: 1, tt_requirenextclick: false, tt_onLoad: __$("nextButton").style.display = "none"; showCategory("Reason For Special Care"); __$("category").style.fontSize = "30px"]
O.1.2.1. Yes
O.1.2.2. No

Q.1.3. 2 or more children in family have died? [helpText: Family has two or more children who died?, pos: 2, tt_requirenextclick: false, tt_onLoad: __$("nextButton").style.display = "none"; showCategory("Reason For Special Care"); __$("category").style.fontSize = "30px"]
O.1.3.1. Yes
O.1.3.2. No

Q.1.4. Child exposed to HIV? [helpText: Child is exposed to HIV?, pos: 3, tt_requirenextclick: false, tt_onLoad: try{$("touchscreenInput" + tstCurrentPage).value = "<%= @patient.is_exposed? rescue nil%>"}catch(c){}; __$("nextButton").style.display = "none"; showCategory("Reason For Special Care"); __$("category").style.fontSize = "30px"]
O.1.4.1. Yes
O.1.4.2. No

Q.1.5. Is child an orphan? [helpText: Child is an orphan?, concept: Orphan, pos: 4, tt_requirenextclick: false, tt_onLoad: __$("nextButton").style.display = "none"; showCategory("Reason For Special Care"); __$("category").style.fontSize = "30px"]
O.1.5.1. Yes
O.1.5.2. No

Q.1.6. Fifth or more child [helpText: Child is fifth (or more) in family?, pos: 5, tt_requirenextclick: false, tt_onLoad: __$("nextButton").style.display = "none"; showCategory("Reason For Special Care"); __$("category").style.fontSize = "30px"]
O.1.6.1. Yes
O.1.6.2. No

Q.1.7. Child a twin [helpText: Child was born as twins?, pos: 6, tt_requirenextclick: false, tt_onLoad: try{$("touchscreenInput" + tstCurrentPage).value = "<%= @patient.twin_outcome? rescue nil%>"}catch(c){}; __$("nextButton").style.display = "none"; showCategory("Reason For Special Care"); __$("category").style.fontSize = "30px"]
O.1.7.1. Yes
O.1.7.2. No

Q.1.8. Any other reason for special care [pos: 7, tt_onLoad: __$("nextButton").style.display = "block"; showCategory("Reason For Special Care"); __$("category").style.fontSize = "30px"]
O.1.8.1. No
O.1.8.2. Yes
Q.1.8.2.1. Specify other reason for special care [concept: Specify, pos: 8, tt_onLoad: __$("nextButton").style.display = "block"; showCategory("Reason For Special Care"); __$("category").style.fontSize = "30px"]

C.1.9. If the child has any of the issues true in #5.1.1 to #5.1.8, the child needs special care


