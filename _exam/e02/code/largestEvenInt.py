
def indexLargestEvenInt_a(ilist):

    if type(ilist)!=list:
        raise ValueError("not a list")
    answer=None
    for x in ilist:
      if x%2 == 0:
        if answer==None or x > answer:
          answer = x
    return answer
	  
def indexLargestEvenInt_b(ilist):

    if type(ilist)!=list:
        raise ValueError("not a list")
    answer=None
    for i in range(len(ilist)):
      if ilist[i]%2 == 0:
        if answer==None or ilist[i] > ilist[answer]:
          answer = i
    return answer
	  
def indexLargestEvenInt_c(ilist):

    if type(ilist)!=list:
        raise ValueError("not a list")
    answer=None
    for i in range(len(ilist)):
      if ilist[i]%2 == 0:
        if answer==None or ilist[i] > ilist[answer]:
          answer = i
      return answer
	  
def indexLargestEvenInt_d(ilist):

    if type(ilist)!=list:
        raise ValueError("not a list")
    answer=None
    for x in ilist:
      if (x%2 == 0) and x > answer:
        answer = x
    return answer


indexLargestEvenInt = indexLargestEvenInt_b

list1 = [22,55,88,33,66]
list2 = [33,33,11,77]
list3 = [33,34,11,66,99]
list4 = [44,11,22]

def test_a_1():
    assert indexLargestEvenInt_a(list1)==2

def test_a_2():
    assert indexLargestEvenInt_a(list2)==None

def test_a_3():
    assert indexLargestEvenInt_a(list3)==3

def test_a_4():
    assert indexLargestEvenInt_a(list4)==0


def test_b_1():
    assert indexLargestEvenInt_b(list1)==2

def test_b_2():
    assert indexLargestEvenInt_b(list2)==None

def test_b_3():
    assert indexLargestEvenInt_b(list3)==3

def test_b_4():
    assert indexLargestEvenInt_b(list4)==0


def test_c_1():
    assert indexLargestEvenInt_c(list1)==2

def test_c_2():
    assert indexLargestEvenInt_c(list2)==None

def test_c_3():
    assert indexLargestEvenInt_c(list3)==3

def test_c_4():
    assert indexLargestEvenInt_c(list4)==0


def test_d_1():
    assert indexLargestEvenInt_d(list1)==2

def test_d_2():
    assert indexLargestEvenInt_d(list2)==None

def test_d_3():
    assert indexLargestEvenInt_d(list3)==3

def test_d_4():
    assert indexLargestEvenInt_d(list4)==0
