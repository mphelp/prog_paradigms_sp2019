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
(define equaltree?
	(lambda (t1 t2)
		(cond
			((and	(null? t1)(null? t2)) #t)
			((and (null? (car t1))(null? (car t2)))(equaltree? (cdr t1)(cdr t2)))
			((and (atom? (car t1))(atom? (car t2)))(cond
					((eq? (car t1)(car t2))(equaltree? (cdr t1)(cdr t2)))
					(else #f)))
			(else (and (equaltree? (car t1)(car t2))(equaltree? (cdr t1)(cdr t2))))
)	)	)
;; 3
(define sub1
	(lambda (a)
		(- a 1)))
(define x
	(lambda (n1 n2)
		(cond
			((zero? n2) 0)
			(else (+ n1 (x (sub1 n2) n1)))
)	)	)



;; Tests
;; 1
(define mylist '((car) car (((y car)))))
(define myanswer 3)
(define test1 
	(cond
		((eq? myanswer (occur* 'car mylist ))'(1 occur* works))
		(else '(1 occur* fails))))
(display test1)
(display "\n")
;; 2
(define mylist1 '(() car (who)))
(define mylist2 '(() car (who)))
(define test2 
	(cond
		((equaltree? mylist1 mylist2)'(2 equaltree works))
		(else '(2 equaltree fails))))
(display test2)
(display "\n")
;; 3
(define test3
	(cond
		((eq? 10 (x 5 2))'(3 x works))
		(else '(3 x fails))))
(display test3)
(display "\n")
