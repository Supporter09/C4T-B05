huy = {
    "name" : "Huy",
    "Role" : "Waiter",
    "Hours": 12,
    "Salary per Hour": 0.8,
}

tung = {
    "name" : "Tung",
    "Role" : "Cook",
    "Hours": 24,
    "Salary per Hour": 1.5,
}

mduc = {
    "name" : "mduc",
    "Role" : "Manager",
    "Hours": 20,
    "Salary per Hour": 2,
}

don = {
    "name" : "Don",
    "Role" : "Waiter",
    "Hours": 12,
    "Salary per Hour": 0.9,
}
hduc = {
    "name" : "H.Duc",
    "Role" : "Waiter",
    "Hours": 14,
    "Salary per Hour": 0.7,
}
res_staff = [huy,tung,mduc,don,hduc]
print("Truoc khi xoa:",res_staff)
res_staff.pop(len(res_staff)-1)
print("Da xoa:",res_staff)