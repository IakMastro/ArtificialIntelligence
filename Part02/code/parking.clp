; Deutero meros ergasias
; Foithths: Iakovos Mastrogiannopoulos
; AM: cse242017102
; Programma Spoudwn: PADA (5etes)

(deftemplate space
    (slot name)
    (slot level)
    (slot state)
)

(deffacts space-init
    (space (name s1) (level 1) (state Y))
    (space (name s2) (level 1) (state N))
    (space (name s3) (level 1) (state Y))
    (space (name s4) (level 1) (state Y))
    (space (name s5) (level 1) (state Y))
    (space (name s6) (level 1) (state Y))
    (space (name s7) (level 2) (state N))
    (space (name s8) (level 2) (state Y))
    (space (name s9) (level 2) (state Y))
    (space (name s10) (level 2) (state Y))
    (space (name s11) (level 2) (state Y))
    (space (name s12) (level 2) (state N))
    (space (name s13) (level 3) (state N))
    (space (name s14) (level 3) (state Y))
    (space (name s15) (level 3) (state Y))
    (space (name s16) (level 3) (state Y))
    (space (name s17) (level 3) (state Y))
    (space (name s18) (level 3) (state Y))
)

(deftemplate platform
    (slot name)
    (slot space)
    (slot plat_state)
)

(deffacts plat-init
    (platform (name p1) (space s1) (plat_state E))
    (platform (name p2) (space s3) (plat_state E))
    (platform (name p3) (space s4) (plat_state E))
    (platform (name p4) (space s5) (plat_state E))
    (platform (name p5) (space s6) (plat_state E))
    (platform (name p6) (space s8) (plat_state E))
    (platform (name p7) (space s9) (plat_state E))
    (platform (name p8) (space s10) (plat_state E))
    (platform (name p9) (space s11) (plat_state E))
    (platform (name p10) (space s14) (plat_state E))
    (platform (name p11) (space s15) (plat_state E))
    (platform (name p12) (space s16) (plat_state E))
    (platform (name p13) (space s17) (plat_state E))
    (platform (name p14) (space s18) (plat_state E))
)

(deftemplate info
    (slot cars_left)
    (slot current_space)
    (slot state)
)

(deftemplate car_to_find
    (slot license_plate)
)

(deftemplate car
    (slot license_plate)
    (slot platform)
)

(defrule startup
    (declare (salience 100))
    (initial-fact)
=>
    (set-strategy random)
    (printout t "Starting the program!" crlf)

    (printout t "Enter the ammount of cars waiting in the line." crlf)
    (bind ?c(read))
    (if (<= ?c 0)
    then
        (printout t "The ammount of cars cannot be 0 or less than 0." crlf)
        (assert (info (cars_left 0) (current_space s2) (state GOAL_NOT_FOUND)))

    else
        (assert (info (cars_left ?c) (current_space s2) (state GOAL_NOT_FOUND)))
    )
)

(defrule goal_found
    (declare (salience 100))
    ?c<-(info (cars_left 0) (state GOAL_NOT_FOUND))
=>
    (modify ?c (state GOAL_FOUND))
    (printout t "Goal found. End of program." crlf)
)

; Kanonas pou rwtaei ton xristi ean thelei na kseparkarei autokinhto
(defrule prompt
    (declare (salience 100))
    ?c<-(info (state PROMPT))
=>
    (printout t "Do you want to remove a car? y/n" crlf)
    (bind ?qu(read))
    (if (eq ?qu y)
    then
        (printout t "Give license plate." crlf)
        (bind ?lp(read)) ; Ean nai, tote pairnei to license plate kai arxizei na to psaxnei
        (modify ?c (state SEARCH_CAR))
        (assert (car_to_find (license_plate ?lp)))

    else
        (modify ?c (state BACK_TO_S2)) ; Ean oxi, tote gurnaei pisw sto s2
    )
)

(deffacts east
    (east s1 s2)
    (east s2 s3)
    (east s4 s5)
    (east s5 s6)
    (east s7 s8)
    (east s8 s9)
    (east s10 s11)
    (east s11 s12)
    (east s13 s14)
    (east s14 s15)
    (east s16 s17)
    (east s17 s18)
)

(defrule moveEast
    ?z<-(space (name ?y) (state N))
    (east ?y ?x)
    ?p<-(space (name ?x) (state Y))
    ?q<-(platform (name ?pn) (space ?x) (plat_state ?ps))
    ?c<-(info (cars_left ?cars) (current_space ?y) (state GOAL_NOT_FOUND)) ; Koitame kai to space pou eimaste twra
=>
    (modify ?p (state N))
    (modify ?z (state Y))

    (if (eq ?ps F)
    then
        (modify ?q (space ?y))
        (modify ?c (current_space ?x))

    else
        (printout t "Enter the license plate." crlf)
        (bind ?lp(read))
        (assert (car (license_plate ?lp) (platform ?pn)))
        (modify ?q (space ?y) (plat_state F))
        (modify ?c (cars_left (- ?cars 1)) (current_space ?x) (state PROMPT)) ; State pou mas paei sto prompt
    )
)

(defrule backToS2East
    ?z<-(space (name ?y) (state N))
    (east ?y ?x)
    ?p<-(space (name ?x) (state Y))
    ?q<-(platform (space ?x))
    ?c<-(info (state BACK_TO_S2) (current_space ?y))
=>
    (modify ?p (state N))
    (modify ?z (state Y))
    (modify ?q (space ?y))
    (if (eq ?x s2)
    then
        (modify ?c (current_space ?x) (state GOAL_NOT_FOUND))

    else
        (modify ?c (current_space ?x))
    )
)

(defrule findCarEast
    ?z<-(space (name ?y) (state N))
    (east ?y ?x)
    ?p<-(space (name ?x) (state Y))
    ?q<-(platform (name ?pn) (space ?x))
    ?car<-(car (license_plate ?lp) (platform ?pn)) ; Autokinhto pou vriskete sthn pn platforma kai exei lp license plate
    ?c<-(info (state SEARCH_CAR))
    ?cf<-(car_to_find (license_plate ?lpf)) ; Euresi lpf license plate
=>
    (modify ?p (state N))
    (modify ?z (state Y))
    (modify ?q (space ?y))
    (if (eq ?lp ?lpf)
    then
        (retract ?car ?cf) ; Afairesh autokinhtou apo thn lista
        (modify ?c (current_space ?x) (state BACK_TO_S2))

    else
        (modify ?c (current_space ?x))
    )
)

(deffacts north
    (north s1 s4)
    (north s2 s5)
    (north s3 s6)
    (north s7 s10)
    (north s8 s11)
    (north s9 s12)
    (north s13 s16)
    (north s14 s17)
    (north s15 s18)
)

(defrule moveNorth
    ?z<-(space (name ?y) (state N))
    (north ?y ?x)
    ?p<-(space (name ?x) (state Y))
    ?q<-(platform (name ?pn) (space ?x) (plat_state ?ps))
    ?c<-(info (cars_left ?cars) (current_space ?y) (state GOAL_NOT_FOUND))
=>
    (modify ?p (state N))
    (modify ?z (state Y))

    (if (eq ?ps F)
    then
        (modify ?q (space ?y))
        (modify ?c (current_space ?x))

    else
        (printout t "Enter the license plate." crlf)
        (bind ?lp(read))
        (assert (car (license_plate ?lp) (platform ?pn)))
        (modify ?q (space ?y) (plat_state F))
        (modify ?c (cars_left (- ?cars 1)) (current_space ?x) (state PROMPT))
    )
)

(defrule backToS2North
    ?z<-(space (name ?y) (state N))
    (north ?y ?x)
    ?p<-(space (name ?x) (state Y))
    ?q<-(platform (space ?x))
    ?c<-(info (state BACK_TO_S2) (current_space ?y))
=>
    (modify ?p (state N))
    (modify ?z (state Y))
    (modify ?q (space ?y))
    (if (eq ?x s2)
    then
        (modify ?c (current_space ?x) (state GOAL_NOT_FOUND))

    else
        (modify ?c (current_space ?x))
    )
)

(defrule findCarNorth
    ?z<-(space (name ?y) (state N))
    (north ?y ?x)
    ?p<-(space (name ?x) (state Y))
    ?q<-(platform (name ?pn) (space ?x))
    ?car<-(car (license_plate ?lp) (platform ?pn))
    ?c<-(info (state SEARCH_CAR))
    ?cf<-(car_to_find (license_plate ?lpf))
=>
    (modify ?p (state N))
    (modify ?z (state Y))
    (modify ?q (space ?y))
    (if (eq ?lp ?lpf)
    then
        (retract ?car ?cf)
        (modify ?c (current_space ?x) (state BACK_TO_S2))

    else
        (modify ?c (current_space ?x))
    )
)

(deffacts west
    (west s2 s1)
    (west s3 s2)
    (west s5 s4)
    (west s6 s5)
    (west s8 s7)
    (west s9 s8)
    (west s11 s10)
    (west s12 s11)
    (west s14 s13)
    (west s15 s14)
    (west s17 s16)
    (west s18 s17)
)

(defrule moveWest
    ?z<-(space (name ?y) (state N))
    (west ?y ?x)
    ?p<-(space (name ?x) (state Y))
    ?q<-(platform (name ?pn) (space ?x) (plat_state ?ps))
    ?c<-(info (cars_left ?cars) (current_space ?y) (state GOAL_NOT_FOUND))
=>
    (modify ?p (state N))
    (modify ?z (state Y))

    (if (eq ?ps F)
    then
        (modify ?q (space ?y))
        (modify ?c (current_space ?x))

    else
        (printout t "Enter the license plate." crlf)
        (bind ?lp(read))
        (assert (car (license_plate ?lp) (platform ?pn)))
        (modify ?q (space ?y) (plat_state F))
        (modify ?c (cars_left (- ?cars 1)) (current_space ?x) (state PROMPT))
    )
)

(defrule backToS2West
    ?z<-(space (name ?y) (state N))
    (west ?y ?x)
    ?p<-(space (name ?x) (state Y))
    ?q<-(platform (space ?x))
    ?c<-(info (state BACK_TO_S2) (current_space ?y))
=>
    (modify ?p (state N))
    (modify ?z (state Y))
    (modify ?q (space ?y))
    (if (eq ?x s2)
    then
        (modify ?c (current_space ?x) (state GOAL_NOT_FOUND))

    else
        (modify ?c (current_space ?x))
    )
)

(defrule findCarWest
    ?z<-(space (name ?y) (state N))
    (west ?y ?x)
    ?p<-(space (name ?x) (state Y))
    ?q<-(platform (name ?pn) (space ?x))
    ?car<-(car (license_plate ?lp) (platform ?pn))
    ?c<-(info (state SEARCH_CAR))
    ?cf<-(car_to_find (license_plate ?lpf))
=>
    (modify ?p (state N))
    (modify ?z (state Y))
    (modify ?q (space ?y))
    (if (eq ?lp ?lpf)
    then
        (retract ?car ?cf)
        (modify ?c (current_space ?x) (state BACK_TO_S2))

    else
        (modify ?c (current_space ?x))
    )
)

(deffacts south
    (south s4 s1)
    (south s5 s2)
    (south s6 s3)
    (south s10 s7)
    (south s11 s8)
    (south s12 s9)
    (south s16 s13)
    (south s17 s14)
    (south s18 s15)
)

(defrule moveSouth
    ?z<-(space (name ?y) (state N))
    (south ?y ?x)
    ?p<-(space (name ?x) (level 1) (state Y))
    ?q<-(platform (name ?pn) (space ?x) (plat_state ?ps))
    ?c<-(info (cars_left ?cars) (current_space ?y) (state GOAL_NOT_FOUND))
=>
    (modify ?p (state N))
    (modify ?z (state Y))

    (if (eq ?ps F)
    then
        (modify ?q (space ?y))
        (modify ?c (current_space ?x))

    else
        (printout t "Enter the license plate." crlf)
        (bind ?lp(read))
        (assert (car (license_plate ?lp) (platform ?pn)))
        (modify ?q (space ?y) (plat_state F))
        (modify ?c (cars_left (- ?cars 1)) (current_space ?x) (state PROMPT))
    )
)

(defrule findCarSouth
    ?z<-(space (name ?y) (state N))
    (south ?y ?x)
    ?p<-(space (name ?x) (state Y))
    ?q<-(platform (name ?pn) (space ?x))
    ?car<-(car (license_plate ?lp) (platform ?pn))
    ?c<-(info (state SEARCH_CAR))
    ?cf<-(car_to_find (license_plate ?lpf))
=>
    (modify ?p (state N))
    (modify ?z (state Y))
    (modify ?q (space ?y))
    (if (eq ?lp ?lpf)
    then
        (retract ?car ?cf)
        (modify ?c (current_space ?x) (state BACK_TO_S2))

    else
        (modify ?c (current_space ?x))
    )
)

(defrule backToS2South
    ?z<-(space (name ?y) (state N))
    (south ?y ?x)
    ?p<-(space (name ?x) (state Y))
    ?q<-(platform (space ?x))
    ?c<-(info (state BACK_TO_S2) (current_space ?y))
=>
    (modify ?p (state N))
    (modify ?z (state Y))
    (modify ?q (space ?y))
    (if (eq ?x s2)
    then
        (modify ?c (current_space ?x) (state GOAL_NOT_FOUND))

    else
        (modify ?c (current_space ?x))
    )
)

(deffacts up
    (up s5 s11)
    (up s11 s17)
)

(defrule moveUp
    ?z<-(space (name ?y) (state N))
    (up ?y ?x)
    ?p<-(space (name ?x) (state Y))
    ?q<-(platform (name ?pn) (space ?x) (plat_state ?ps))
    ?c<-(info (cars_left ?cars) (current_space ?y) (state GOAL_NOT_FOUND))
=>
    (modify ?p (state N))
    (modify ?z (state Y))

    (if (eq ?ps F)
    then
        (modify ?q (space ?y))
        (modify ?c (current_space ?x))

    else
        (printout t "Enter the license plate." crlf)
        (bind ?lp(read))
        (assert (car (license_plate ?lp) (platform ?pn)))
        (modify ?q (space ?x) (plat_state F))
        (modify ?c (cars_left (- ?cars 1)) (current_space ?x) (state PROMPT))
    )
)

(defrule findCarUp
    ?z<-(space (name ?y) (state N))
    (up ?y ?x)
    ?p<-(space (name ?x) (state Y))
    ?q<-(platform (name ?pn) (space ?x))
    ?car<-(car (license_plate ?lp) (platform ?pn))
    ?c<-(info (state SEARCH_CAR))
    ?cf<-(car_to_find (license_plate ?lpf))
=>
    (modify ?p (state N))
    (modify ?z (state Y))
    (modify ?q (space ?y))
    (if (eq ?lp ?lpf)
    then
        (retract ?car ?cf)
        (modify ?c (current_space ?x) (state BACK_TO_S2))

    else
        (modify ?c (current_space ?x))
    )
)

(deffacts down
    (down s11 s5)
    (down s17 s11)
)

(defrule moveDown
    ?z<-(space (name ?y) (state N))
    (down ?y ?x)
    ?p<-(space (name ?x) (state Y))
    ?q<-(platform (name ?pn) (space ?x) (plat_state ?ps))
    ?c<-(info (cars_left ?cars) (current_space ?y) (state GOAL_NOT_FOUND))
=>
    (modify ?p (state N))
    (modify ?z (state Y))

    (if (eq ?ps F)
    then
        (modify ?q (space ?y))
        (modify ?c (current_space ?x))

    else
        (printout t "Enter the license plate." crlf)
        (bind ?lp(read))
        (assert (car (license_plate ?lp) (platform ?pn)))
        (modify ?q (space ?y) (plat_state F))
        (modify ?c (cars_left (- ?cars 1)) (current_space ?x) (state PROMPT))
    )
)

(defrule findCarDown
    ?z<-(space (name ?y) (state N))
    (down ?x ?y)
    ?p<-(space (name ?x) (state Y))
    ?q<-(platform (name ?pn) (space ?x))
    ?car<-(car (license_plate ?lp) (platform ?pn))
    ?c<-(info (state SEARCH_CAR))
    ?cf<-(car_to_find (license_plate ?lpf))
=>
    (modify ?p (state N))
    (modify ?z (state Y))
    (modify ?q (space ?y))
    (if (eq ?lp ?lpf)
    then
        (retract ?car ?cf)
        (modify ?c (current_space ?x) (state BACK_TO_S2))

    else
        (modify ?c (current_space ?x))
    )
)