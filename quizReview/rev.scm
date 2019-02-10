(load-from-path "/escnfs/home/cmc/public/paradigms/scheme/d1/paradigms_d1.scm")
;;
(use-modules (ice-9 paradigms_d3))

;; 1
(define occur*
	(lambda (a l)
		(cond
			((null? l) 0)
			((lat? l)(cond
					((null? l) 0)
					((eq? a (car l))(+ 1 (occur* a (cdr l))))
					(else (occur* a (cdr l)))))
			(else + (occur* a (car l))(occur* a (cdr l)))
)	)	)






;; Tests
(define test1 
	(cond
		((eq? 2 (occur* 'car '(car y y car u)))'(1 occur* works))
		(else '(1 occur* fails))))
(display test1)
(display "\n")
