;; scheme tictactoe homework
;; name: ??????????
;; date: ??????????

(include "/escnfs/home/cmc/public/paradigms/scheme/ttt/paradigms_ttt.scm")

;; REPLACE WITH YOUR FUNCTIONS FROM A PREVIOUS HOMEWORK:
;;  greatest
;;  positionof
;;  value

(define greatest
  (lambda (tup)
    0))

(define positionof
  (lambda (a tup)
    0))

(define value
  (lambda (p gs)
    0))

;; MODIFY your sum* function for this assignment...
(define sum*-g
  (lambda (ttup f)
    0))

;; MODIFY this function so that given the game tree 
;; (where the current situation is at the root),
;; it returns the recommendation for the next move
(define nextmove
  (lambda (p gt)
    (car gt)))

;; onegametree is defined in paradigms_ttt
;; be sure to look at that file!

;; what is the current game situation?
(display "Current State:     ")
(display (car (onegametree)))
(display "\n")

;; test of nextmove, where should we go next?
(display "Recommended Move:  ")
(display (nextmove 'x (onegametree)))
(display "\n")

;; correct output:
;;   $ guile tictactoe.scm
;;   Current State:     (x o x o o e e x e)
;;   Recommended Move:  (x o x o o x e x e)

