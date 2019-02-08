;; scheme tictactoe homework
;; name: Matthew Phelps
;; date: Feb 7 2019

(include "/escnfs/home/cmc/public/paradigms/scheme/ttt/paradigms_ttt.scm")

;; REPLACE WITH YOUR FUNCTIONS FROM A PREVIOUS HOMEWORK:
;;  greatest
;;  positionof
;;  value

(define greatest
  (lambda (tup)
		(cond
			((null? (cdr tup))(car tup))
			((> (car tup)(greatest (cdr tup)))(car tup))
			(else (greatest (cdr tup)))
) ) )

(define positionof
  (lambda (a tup)
		(cond
			((eq? n (car tup))'1)
			(else (+ 1 (positionof n (cdr tup))))
)	)	)

(define value
	(lambda (p)
		(lambda (gs)
			(cond
				((win? p gs)'10)
				((win? (other p) gs)'-10)
				(else '0)
)	)	) )

;; MODIFY your sum* function for this assignment...
(define sum*-g
  (lambda (ttup f)
		(cond
			((null? ttup) 0)
			((null? (cdr ttup))(f (car ttup)))
			(else (+ (sum*-g (car (cdr ttup)) f)(sum*-g (cons (car ttup)(cdr (cdr ttup))) f)))
)	)	)

;;(define valuex
;;	(lambda (gs)
;;		((value 'x) gs)
;;)	)
;; MODIFY this function so that given the game tree 
;; (where the current situation is at the root),
;; it returns the recommendation for the next move
(define nextmove
  (lambda (p gt)
    (car gt)))

;; onegametree is defined in paradigms_ttt
;; be sure to look at that file!

;; what is the current game situation?
;;(display "Current State:     ")
;;(display (car (onegametree)))
;;(display "\n")

;; test of nextmove, where should we go next?
;;(display "Recommended Move:  ")
;;(display (nextmove 'x (onegametree)))
;;(display "\n")

;;(display "testing value\n")
;;(display (car (car (cdr (onegametree)))))
;;(display "\n")
;;(display ((value 'o) (car (car (cdr (onegametree))))))
;;(display (sum*-g (onegametree) (value 'x)))
;;(display "\n")
;; correct output:
;;   $ guile tictactoe.scm
;;   Current State:     (x o x o o e e x e)
;;   Recommended Move:  (x o x o o x e x e)

(display (sum*-g (car (cdr (onegametree))) (value 'x)))
(display "\n")
(display (sum*-g (onegametree) (value 'o)))
(display "\n")
