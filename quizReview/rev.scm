(include "/escnfs/home/cmc/public/paradigms/scheme/d1/paradigms_d1.scm")
;;

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
(define mylist '((car)))
(define test1 
	(cond
		((eq? 1 (occur* 'car mylist ))'(1 occur* works))
		(else '(1 occur* fails))))
(display (occur* 'car mylist)) 
(display "\n")
(display test1)
(display "\n")
