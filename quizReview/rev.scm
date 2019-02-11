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
;; 4
(define member?
	(lambda (a lat)
		(cond
			((null? lat) #f)
			((eq? a (car lat)) #t)
			(else (member? a (cdr lat))))))
(define makeset
	(lambda (lat)
		(cond	
			((null? lat)'())
			((member? (car lat) (cdr lat))(makeset (cdr lat)))
			(else (cons (car lat) (makeset (cdr lat))))
)	)	)
;; 5
(define addup
	(lambda (tup)
		(cond
			((null? tup) 0)
			(else (+ (car tup)(addup (cdr tup)))))))
(define addtups
	(lambda (l)
		(cond
			((null? l) '())
			(else (cons (addup (car l))(addtups (cdr l))))
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
;; 4
(define test4
	(cond
		((equaltree? '(3) (makeset '(3 3)))'(4 makeset works))
		(else '(4 makeset fails))))
(display test4)
(display "\n")
;; 5
(define test5
	(cond
		((equaltree? '(4 5 6) (addtups '((3 1)(0 5)(4 2))))'(6 addtups works))
		(else '(6 addtups fails))))
(display test5)
(display "\n")
