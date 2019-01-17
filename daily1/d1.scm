;; this is how to load external modules in scheme
(load-from-path "/escnfs/home/cmc/public/paradigms/scheme/d1/paradigms_d1.scm")
(use-modules (ice-9 paradigms_d1))

;; Matthew Phelps, Jan 16 2019

;; the list q
;; notice it has a ' in front of the list; that tells the interpreter to read
;; the list literally (e.g., as atoms, instead of functions)
(define q '(turkey (gravy) (stuffing potatoes ham) peas))

;; question 1
(display "question 1: ")
(display (atom? (car (cdr (cdr q)))))
(display "\n")
;; output:
;; question 1: #f

;; explanation:
;; -- The car of the cdr of the cdr of the list q is another list
;;    i.e. (stuffing potatoes ham) and thus the function atom? returns FALSE
;; -- Procedure in full:
;; 			atom? (car (cdr (cdr (turkey (gravy) (stuffing potatoes ham) peas))))
;; 			atom? (car (cdr ((gravy) (stuffing potatoes ham) peas)))
;; 			atom? (car ((stuffing potatoes ham) peas))
;; 			atom? ((stuffing potatoes ham))
;;   		#f


;; question 2
(display "question 2: ")
(display (lat? (car (cdr (cdr q)))))
(display "\n")
;; output:
;; question 2: #t
;;
;; explanation:
;; -- The list above (stuffing potatoes ham) here is the result once again of car (cdr (cdr q))
;;   	Rather than asking if the list is an atom, lat? asks if it is a list of atoms,
;;    to which the correct value is returned: true i.e. #t
;;


;; question 3
(display "question 3: ")
(display (cond ((atom? (car q)) (car q)) (else '())))
(display "\n")
;; output:
;; question 3: turkey
;;
;; explanation:
;; NOTE, in your explanation, be sure to explain what 'cond' and 'else' are.

;; -- "cond" is a procedure which evaluates the test (atom ? (car q)) and if this expression
;; 		is true, which it is, the corresponding sequence after it (car q) is returned.

;; -- the optional "else" clause is a procedure that is evaluated if none of the
;; 		preceding tests yields a true value

