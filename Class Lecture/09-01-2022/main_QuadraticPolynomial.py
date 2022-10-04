import oop_intro as qp

answer_quest = "yes"
while(answer_quest == "yes"):
    a, b, c = input("Please type the coefficients of your equation: ").split()
    a = float(a)
    b = float(b)
    c = float(c)
    poly = qp.quadratic_polynomial(a,b,c)
    poly.general_formula()
    h, k = poly.vertex_formula()
    print("\nThe vertex of this quadratic polynomial is ({0:.5},{1:.5})".format(h,k))
    poly.plot_function()
    answer_quest = input("\nDo you want to keep using the application? ")