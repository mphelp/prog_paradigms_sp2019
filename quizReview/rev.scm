;; 1
(define occur
	(lambda (a lat)
		(cond
			((null? lat) 0)
			((eq? a (car lat))(+ 1 (occur a (cdr lat))))
			(else (occur a (cdr lat)))
)	)	)






;; Tests
(define test1 
	(cond
		((eq? 2 (occur 'car '(car y y car u)))'(1 occur works))
		(else '(1 occur fails))))
(display test1)
(display "\n")
