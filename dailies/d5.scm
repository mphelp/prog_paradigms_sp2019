;; Matthew Phelps
;; Jan 26 2019

;; utility functions, finish these first!
(define firsts
	(lambda (lat)
		(cond
			((null? lat) '())
			(else (cons (car (car lat))(firsts (cdr lat))))
)	)	)

(define member?
	(lambda (a lat)
		(cond
			((null? lat) #f)
			((eq? a (car lat)) #t)
			(else (member? a (cdr lat)))
)	)	)

(define subset?
	(lambda (s1 s2)
		(cond
			((null? s1) #t)
			((member? (car s1) s2)(subset? (cdr s1) s2))
			(else #f)
)	)	)

;; data variables
(define dict  '((t o m a t o) (f i r e) (s a u c e) (c h i c k e n) (f r i e d) (f l a m e s)))
(define words '((o i l p r e s s u r e) (o i l t e m p) (m a g n e t i c c o m p a s s) (s e a t b e l t s) (e l t) (a i r s p e e d) (a l t i m e t e r) (t a c h o m e t e r) (m a n i f o l d) (f u e l g a u g e) (t e m p g a u g e) (l a n d i n g g e a r l i g h t)))

;; acronym finder
(define acronyms
;; your code here ;-)
;; be sure to build your code using the utility functions from above

(display (acronyms dict words))
(display "\n")

;; output should be:
;; ((t o m a t o) (f l a m e s))

