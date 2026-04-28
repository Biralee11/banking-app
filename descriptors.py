class BalanceDescriptor():
    def __get__(self, obj, objtype):
        return obj._balance

    def __set__(self, obj, value):
        if not isinstance(value, (int, float)):
            print("Balance must be a number.")
            return
        if value >= 0:
            obj._balance = value
        else:
            print("Balance cannot be less than zero.")

    def __delete__(self, obj):
        print("Balance cannot be deleted")

class CurrentAccountBalanceDescriptor():
    def __get__(self, obj, objtype):
        return obj._balance
    
    def __set__(self, obj, value):
        if not isinstance(value, (int, float)):
            print("Balance must be a number.")
            return
        if value >= (-obj.overdraft_limit):
            obj._balance = value
        else:
            print("Balance cannot be less than overdraft limit.")

    def __delete__(self, obj):
        print("Balance cannot be deleted")