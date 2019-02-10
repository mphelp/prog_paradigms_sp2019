(include "/escnfs/home/cmc/public/paradigms/scheme/d1/paradigms_d1.scm")
;;

;; 1
(define occur*
	(lambda (a l)
		(cond
			((null? l) 0)
			((atom? (car l))(cond
					((eq? a (car l))(+ 1 (occur* a (cdr l))))
					(else (occur* a (cdr l)))))
			(else (+ (occur* a (car l))(occur* a (cdr l))))
)	)	)

;; 2
(define equaltree '())




;; Tests
(define mylist '((car) car (((y car)))))
(define myanswer 3)
(define test1 
	(cond
		((eq? myanswer (occur* 'car mylist ))'(1 occur* works))
		(else '(1 occur* fails))))
(display test1)
(display "\n")
