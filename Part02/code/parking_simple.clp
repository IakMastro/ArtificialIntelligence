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
)

(deftemplate car
    (slot cars_left)
    (slot state)
)

; Kanonas pou ksekinaei to programma
(defrule startup
    (declare (salience 100)) ; Dinei protereotita ston kanona
    (initial-fact)
=>
    (set-strategy random)
    (printout t "Starting the program!" crlf)

    (printout t "Enter the ammount of cars waiting in the line." crlf)
    (bind ?c(read)) ; Eisagwgh arithmwn autokitwn pou perimenei sthn oura
    (if (<= ?c 0)
    then
        (printout t "The ammount of cars cannot be 0 or less than 0." crlf)
        (assert (car (cars_left 0) (state GOAL_NOT_FOUND)))
    else
        (assert (car (cars_left ?c) (state GOAL_NOT_FOUND)))
    )
)

; Kanonas pou leitourgh mono ean vrethike to goal
(defrule goal_found
    (declare (salience 100))
    ?c<-(car (cars_left 0) (state GOAL_NOT_FOUND))
=>
    (modify ?c (state GOAL_FOUND))
    (printout t "Goal found. End of program." crlf)
)

(deffacts east
    (east s1 s2)
    (east s2 s3)
    (east s4 s5)
    (east s5 s6)
)

; Kanonas pou kounaei anatolika ton automato parkadoro
(defrule moveEast
    ?z<-(space (name ?y) (state N)) ; Trexon space
    (east ?x ?y)
    ?p<-(space (name ?x) (state Y)) ; Space pou tha paei o parkadoros
    ?q<-(platform (space ?x) (plat_state ?ps)) ; Platforma pou uparxei sto space
    ?c<-(car (cars_left ?cars) (state GOAL_NOT_FOUND)) ; Katastasi autokinhtwn
=>
    (modify ?p (state N)) ; Allagi space state se N gia to space pou tha pame 
    (modify ?z (state Y)) ; Allagi space state se Y gia to space pou eimastan
    (if (eq ?ps F)
    then
        (modify ?q (space ?y))

    else
        (modify ?q (space ?y) (plat_state F)) ; Ean den einai gemato, vazei to autokinito
        (modify ?c (cars_left (- ?cars 1))) ; Afairei 1 apo ta autokinhta pou apomenoun
    )
)

(deffacts north
    (north s1 s4)
    (north s2 s5)
    (north s3 s6)
)

; Kanonas pou kounaei voreia ton automato parkadoro
(defrule moveNorth
    ?z<-(space (name ?y) (state N))
    (north ?x ?y)
    ?p<-(space (name ?x) (state Y))
    ?q<-(platform (space ?x) (plat_state ?ps))
    ?c<-(car (cars_left ?cars) (state GOAL_NOT_FOUND))
=>
    (modify ?p (state N))
    (modify ?z (state Y))
    (if (eq ?ps F)
    then
        (modify ?q (space ?y))

    else
        (modify ?q (space ?y) (plat_state F))
        (modify ?c (cars_left (- ?cars 1)))
    )
)

(deffacts west
    (west s2 s1)
    (west s3 s2)
    (west s5 s4)
    (west s6 s5)
)

; Kanonas pou kounaei dutika ton automato parkadoro
(defrule moveWest
    ?z<-(space (name ?y) (state N))
    (west ?x ?y)
    ?p<-(space (name ?x) (state Y))
    ?q<-(platform (space ?x) (plat_state ?ps))
    ?c<-(car (cars_left ?cars) (state GOAL_NOT_FOUND))
=>
    (modify ?p (state N))
    (modify ?z (state Y))
    (if (eq ?ps F)
    then
        (modify ?q (space ?y))

    else
        (modify ?q (space ?y) (plat_state F))
        (modify ?c (cars_left (- ?cars 1)))
    )
)

(deffacts south
    (south s4 s1)
    (south s5 s2)
    (south s6 s3)
)

; Kanonas pou kounaei notia ton automato parkadoro
(defrule moveSouth
    ?z<-(space (name ?y) (state N))
    (south ?x ?y)
    ?p<-(space (name ?x) (state Y))
    ?q<-(platform (space ?x) (plat_state ?ps))
    ?c<-(car (cars_left ?cars) (state GOAL_NOT_FOUND))
=>
    (modify ?p (state N))
    (modify ?z (state Y))
    (if (eq ?ps F)
    then
        (modify ?q (space ?y))

    else
        (modify ?q (space ?y) (plat_state F))
        (modify ?c (cars_left (- ?cars 1)))
    )
)
