P.1. Reason for special care [program: UNDER 5 PROGRAM]
C.1. Check if child needs special care
Q.1.1. Weight less than 2500g [pos: 0, tt_requirenextclick: false, tt_onLoad: tt_cancel_destination += "&skip_flow=true"; __$("nextButton").style.display = "none"; skipFlow("<%= params["skip_flow"]%>")]
O.1.1.1. Yes
O.1.1.2. No

Q.1.2. Baby born less than 2 years since last birth of other child [pos: 1, tt_requirenextclick: false, tt_onLoad: __$("nextButton").style.display = "none"]
O.1.2.1. Yes
O.1.2.2. No

Q.1.3. 2 or more children in family have died? [pos: 2, tt_requirenextclick: false, tt_onLoad: __$("nextButton").style.display = "none"]
O.1.3.1. Yes
O.1.3.2. No

Q.1.4. Child exposed to HIV? [pos: 3, tt_requirenextclick: false, tt_onLoad: __$("nextButton").style.display = "none"]
O.1.4.1. Yes
O.1.4.2. No

Q.1.5. Is child an orphan? [concept: Orphan, pos: 4, tt_requirenextclick: false, tt_onLoad: __$("nextButton").style.display = "none"]
O.1.5.1. Yes
O.1.5.2. No

Q.1.6. Fifth or more child [pos: 5, tt_requirenextclick: false, tt_onLoad: __$("nextButton").style.display = "none"]
O.1.6.1. Yes
O.1.6.2. No

Q.1.7. Child a twin [pos: 6, tt_requirenextclick: false, tt_onLoad: __$("nextButton").style.display = "none"]
O.1.7.1. Yes
O.1.7.2. No

Q.1.8. Any other reason for special care [pos: 7, tt_onLoad: __$("nextButton").style.display = "block"]
O.1.8.1. No
O.1.8.2. Yes
Q.1.8.2.1. Specify other reason for special care [concept: Specify, pos: 8, tt_onLoad: __$("nextButton").style.display = "block"]

C.1.9. If the child has any of the issues true in #5.1.1 to #5.1.8, the child needs special care


