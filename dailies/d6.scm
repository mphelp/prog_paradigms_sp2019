;; scheme 6
;; name: Matthew Phelps
;; date: Jan 28 2019

;; notice the use of debugging traps when available
;; (use-modules (ice-9 debugging traps) (ice-9 debugging trace))

(define sum*
  (lambda (ttup)
    (cond
			((null? ttup) 0)
			(else (+ (car (car ttup))(sum* (cdr ttup))))
)	)	)

;(install-trap (make <procedure-trap>
;                            #:procedure sum*
;                            #:behaviour (list trace-trap trace-until-exit)))

;; tests!
(display (sum* '((5)) ))
(display "\n")

(display (sum* '((0) ((0) ((5))) ((0) ((10)))) ))
(display "\n")

(display (sum* '((0) ((0) ((5) ((7)))) ((0) ((10) ))) ))
(display "\n")

(display (sum* '((0) ((0) ((5) ((7) ) ((8) ))) ((0) ((10) ))) ))
(display "\n")

;; correct output:
;;   $ guile d6.scm
;;   5
;;   15
;;   22
;;   30

