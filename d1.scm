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
;; (copy the output you saw here)
;;
;; explanation:
;; (use as many lines as necessary, just add more comments)
;;


;; question 2
(display "question 2: ")
(display (lat? (car (cdr (cdr q)))))
(display "\n")
;; output:
;;
;;
;; explanation:
;;
;;


;; question 3
(display "question 3: ")
(display (cond ((atom? (car q)) (car q)) (else '())))
(display "\n")
;; output:
;;
;;
;; explanation:
;; NOTE, in your explanation, be sure to explain what 'cond' and 'else' are.
;;
;;

