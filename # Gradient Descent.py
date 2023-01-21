# Gradient Descent 

# x = float(input())
# eta = float(input()) 
# step = int(input()) # số bước

'''
where cực tiểu của hàm f(x) = x^2-4x+4
đạo hàm f'(x) = 2x+4

eta = 

x(t+1) = x(t) - nf'(x(t))

'''

# for i in range(step):
#     x_new = x - eta*(2*x-4)
#     if abs(2*x_new - 4) < 1e-3:
#         print(f"x_min = %f, loss_function = %f, after %d step"%(x_new, x_new-2, i+1))
#         break
#     x = x_new
# else:
#     print(f"Cannot find x_min after {step} step  with learning rate eta = {eta}")
    

# Huy đi code lại

x = float(input())
eta=float(input())
step=int(input())
for i in range(step):
    x_new = x-eta*(2*x-4)
    if abs(2*x_new-4) < 1e-3:
        print("x_min = %f, loss_function = %f, after %d step"%(x_new,x_new**2- 4*x_new+4,i+1))
        break
    x = x_new
else:
    print(f"Cannot find x_min after {step} with learning rate eta = {eta}")
    
# x = float(input())
# eta=float(input())
# step=int(input())
# for i in range(100):
#     x_new = x -eta*(2*x-4)
#     if abs(2*x_new-4)<1e-3:
#         print("x_min = %f, loss_function = %f, after %d step"%(x_new, x_new**2-4*x_new+4, i+1))
#         break
#     x = x_new
# else:
#     print(f"Cannot find x_min after {step} step with learning rate eta = {eta}")