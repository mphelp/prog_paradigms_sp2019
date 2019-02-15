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
;; 6
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
;; 8
(define pick
	(lambda (n lat)
		(cond
			((zero? (sub1 n))(car lat))
			(else (pick (sub1 n)(cdr lat)))
)	)	)
;; 9
(define insertR*
	(lambda (a b l)
		(cond
			((null? l)'())
			((atom? (car l))(cond
					((eq? a (car l))(cons (car l)(cons b (insertR* a b (cdr l)))))
					(else (cons (car l)(insertR* a b (cdr l))))))
			(else (cons (insertR* a b (car l))(insertR* a b (cdr l))))
)	)	)

;; 11
(define zip
	(lambda (t1 t2)
		(cons (cons (car t1)(list (car t2)))(list (cons (car (cdr t1))(cdr t2))))
)	)


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
;; 6
(define test6
	(cond
		((equaltree? '(4 5 6) (addtups '((3 1)(0 5)(4 2))))'(6 addtups works))
		(else '(6 addtups fails))))
(display test6)
(display "\n")
;; 8
(define test8
	(cond
		((eq? 'duck (pick 3 '(who is duck mcgee)))'(8 pick works))
		(else '(8 pick fails))))
(display test8)
(display "\n")
;; 9
(define mything '(ben (h (ben))))
(define mythingans '(ben major (h (ben major))))
(define test9
	(cond
		((equaltree? mythingans (insertR* 'ben 'major mything))'(9 insertR* works))
		(else '(9 insertR* fails))))
(display test9)
(display "\n")
;; 11
(define before1 '(peas butter))
(define before2 '(carrots toast))
(define after  '((peas carrots)(butter toast)))
(define test11
	(cond
	((equaltree? after (zip before1 before2))'(11 zip works))
		(else '(11 zip fails))))
(display test11)
(display "\n")
