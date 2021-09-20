####################
####################
#Definition: Let p be a proposition. The negation of p, denoted by NOT p (-p) is the statement. 
#The proposition -p is read "not p". The truth value of the negation of p, -p, is the opposite of the truth value of p.
#Constraints: Use 'T', 'F', 1, and 0 respectively as arguments. Returns 'None' if there is an invalid argument. Also prints an exception.  

def negation(truth_value):
	try:
		if truth_value == 'T':
			truth_value = 'F'
			return truth_value
		elif truth_value == 'F':
			truth_value = 'T'
			return truth_value
		elif truth_value == 1:
			truth_value = 0
			return truth_value
		elif truth_value == 0:
			truth_value = 1
			return truth_value
		else:
			raise ValueError

	except ValueError as exception:
		print('Invalid Input, please use T,F,1 or 0 while using this function')
		print('1 argument must be present.')
####################
####################
#Definition: Let p and q be propositions. The conjuction of p and q, denoted by p ^ q, is the proposition "p and q."
#The conjuction p ^ q is true when both p and q are true and false otherwise.
#Constraints: Use 'T', 'F', 1, and 0 respectively as arguments. Returns 'None' if there is an invalid argument. Also prints an exception. 

def conjuction(truth_value_one, truth_value_two):
	truth_value = 0
	try:
		if truth_value_one == 'T' and truth_value_two == 'T':
			truth_value = 'T'
			return truth_value
		elif truth_value_one == 'T' and truth_value_two == 'F':
			truth_value = 'F'
			return truth_value
		elif truth_value_one == 'F' and truth_value_two == 'T':
			truth_value = 'F'
			return truth_value
		elif truth_value_one == 'F' and truth_value_two == 'F':
			truth_value = 'F'
			return truth_value
		elif truth_value_one == 1 and truth_value_two == 1:
			truth_value = 1
			return truth_value
		elif truth_value_one == 1 and truth_value_two == 0:
			truth_value = 0
			return truth_value
		elif truth_value_one == 0 and truth_value_two == 1:
			truth_value = 0
			return truth_value
		elif truth_value_one == 0 and truth_value_two == 0:
			truth_value = 0
			return truth_value
		else:
			raise ValueError

	except ValueError as exception:
		print('Invalid Input, please use T,F,1 or 0 while using this function')
		print('2 arguments must be present.')
####################
####################
#Definition: Let p and q be propositions. The disjunction of p and q, denoted p ∨ q is the proposition "p or q."
#The disjunction p OR q is false when both p and q are false and true otherwise.

def disjunction(truth_value_one, truth_value_two):
	truth_value = 0
	try:
		if truth_value_one == 'T' and truth_value_two == 'T':
			truth_value = 'T'
			return truth_value
		elif truth_value_one == 'T' and truth_value_two == 'F':
			truth_value = 'T'
			return truth_value
		elif truth_value_one == 'F' and truth_value_two == 'T':
			truth_value = 'T'
			return truth_value
		elif truth_value_one == 'F' and truth_value_two == 'F':
			truth_value = 'F'
			return truth_value
		elif truth_value_one == 1 and truth_value_two == 1:
			truth_value = 1
			return truth_value
		elif truth_value_one == 1 and truth_value_two == 0:
			truth_value = 1
			return truth_value
		elif truth_value_one == 0 and truth_value_two == 1:
			truth_value = 1
			return truth_value
		elif truth_value_one == 0 and truth_value_two == 0:
			truth_value = 0
			return truth_value
		else:
			raise ValueError

	except ValueError as exception:
		print('Invalid Input, please use T,F,1 or 0 while using this function')
		print('2 arguments must be present.')
####################
####################
#Definition: Let p and q be propositions. The exclusive of p and q, denoted p ⊕ q, is the proposition
#that is true when exactly one of p and q is true and is false otherwise.

def exclusive_or(truth_value_one, truth_value_two):
	truth_value = 0
	try:
		if truth_value_one == 'T' and truth_value_two == 'T':
			truth_value = 'F'
			return truth_value
		elif truth_value_one == 'T' and truth_value_two == 'F':
			truth_value = 'T'
			return truth_value
		elif truth_value_one == 'F' and truth_value_two == 'T':
			truth_value = 'T'
			return truth_value
		elif truth_value_one == 'F' and truth_value_two == 'F':
			truth_value = 'F'
			return truth_value
		elif truth_value_one == 1 and truth_value_two == 1:
			truth_value = 0
			return truth_value
		elif truth_value_one == 1 and truth_value_two == 0:
			truth_value = 1
			return truth_value
		elif truth_value_one == 0 and truth_value_two == 1:
			truth_value = 1
			return truth_value
		elif truth_value_one == 0 and truth_value_two == 0:
			truth_value = 0
			return truth_value
		else:
			raise ValueError

	except ValueError as exception:
		print('Invalid Input, please use T,F,1 or 0 while using this function')
		print('2 arguments must be present.')
####################
####################
#Definition: Let p and q be propositions. The conditional statment p -> q is the proposition
#"if p, then q." The conditional statement p -> q is false when p is true and q is false, and true otherwise.
#In the conditional statment p -> q, p is called the hypothesis (or antecedent or premise)
#and q is called the conclusion (or consequence)

def conditional(truth_value_one, truth_value_two):
	truth_value = 0
	try:
		if truth_value_one == 'T' and truth_value_two == 'T':
			truth_value = 'T'
			return truth_value
		elif truth_value_one == 'T' and truth_value_two == 'F':
			truth_value = 'F'
			return truth_value
		elif truth_value_one == 'F' and truth_value_two == 'T':
			truth_value = 'T'
			return truth_value
		elif truth_value_one == 'F' and truth_value_two == 'F':
			truth_value = 'T'
			return truth_value
		elif truth_value_one == 1 and truth_value_two == 1:
			truth_value = 1
			return truth_value
		elif truth_value_one == 1 and truth_value_two == 0:
			truth_value = 0
			return truth_value
		elif truth_value_one == 0 and truth_value_two == 1:
			truth_value = 1
			return truth_value
		elif truth_value_one == 0 and truth_value_two == 0:
			truth_value = 1
			return truth_value
		else:
			raise ValueError

	except ValueError as exception:
		print('Invalid Input, please use T,F,1 or 0 while using this function')
		print('2 arguments must be present.')
####################
####################
#Definition: Let p and q be propositions. The biconditional statment p <-> q is the proposition "p if and only if q."
#The biconditional statement p <-> q is true when p and q have the same truth values, and false otherwise.
#Biconditional statments are also called bi-implications.

def biconditional(truth_value_one, truth_value_two):
	truth_value = 0
	try:
		if truth_value_one == 'T' and truth_value_two == 'T':
			truth_value = 'T'
			return truth_value
		elif truth_value_one == 'T' and truth_value_two == 'F':
			truth_value = 'F'
			return truth_value
		elif truth_value_one == 'F' and truth_value_two == 'T':
			truth_value = 'F'
			return truth_value
		elif truth_value_one == 'F' and truth_value_two == 'F':
			truth_value = 'T'
			return truth_value
		elif truth_value_one == 1 and truth_value_two == 1:
			truth_value = 1
			return truth_value
		elif truth_value_one == 1 and truth_value_two == 0:
			truth_value = 0
			return truth_value
		elif truth_value_one == 0 and truth_value_two == 1:
			truth_value = 0
			return truth_value
		elif truth_value_one == 0 and truth_value_two == 0:
			truth_value = 1
			return truth_value
		else:
			raise ValueError

	except ValueError as exception:
		print('Invalid Input, please use T,F,1 or 0 while using this function')
		print('2 arguments must be present.')
####################
####################
#Definition: We can say that, the compound propositions p and q are logically equivalent if p <-> q is a tautology
#The notation p ≡ q denotes that p and q are logically equivalent. 
#Denoted using numbers as it is less prone to error. 
def logical_equivalences(number_law):
	return {
		0: ('Identity laws -->','p AND T ≡ p', 'p OR F ≡ p'),
		1: ('Domination laws -->','p OR T ≡ T', 'p AND q ≡ F'),
		2: ('Idempotent laws -->','p OR p ≡ p', 'p AND p ≡ p'),
		3: ('Double Negation law -->','¬(¬p) ≡ p'),
		4: ('Communative laws -->','p OR q ≡ q OR p', 'p AND q ≡ q AND p'),
		5: ('Associative laws -->','(p OR q) OR r ≡ p OR (q OR r)', '(p AND q) AND r ≡ p AND (q AND r)'),
		6: ('Distributive laws -->','p OR (q AND r) ≡ (p OR q) AND (p OR r)', 'p AND (q OR r) ≡ (p AND q) OR (p AND r)'),
		7: ('De morgan\'s laws -->','¬(p AND q) ≡ ¬p OR¬q', '¬(p OR q) ≡ ¬p AND¬q'),
		8: ('Absorbtion laws -->','p OR (p AND q) ≡ p','p AND (p OR q) ≡ p'),
		9: ('Negation law -->','p OR¬p ≡ T', 'p AND¬p ≡ F')
	}.get(number_law, 'logical equivalence law not found, please use numbers 0 - 9.')