# objectを明示的に継続しなくてもいい
class Daikan:
    def __init__(self, name: str, money: int):
        # 出来ればメンバー変数のスコープを小さくにする（__memberはprivate、_memberはprotected、memberはpublic）
        self._name = name
        self._money = money

    def greet(self):
        print('name:%s money:%d' % (self._name, self._money))


class Akudaikan(Daikan):
    # Pythonは自動的にスーパークラスのコンストラクタを実行しない
    def __init__(self, name: str, money: int):
        super(Akudaikan, self).__init__(name, money)
        # Daikan.__init__(self, name, money)も問題ないですが、おすすめしない
        self.__hidden_money = 0

    def get_sodenosita(self, money: int):
        self.__hidden_money += money

    # メソッドをオーバーライド
    def greet(self):
        print('name:%s money:%d' % (self._name, self._money))
        if self.__hidden_money > 999:
            print('%s is arrested!' % self._name)


if __name__ == '__main__':
    dk = Daikan("daikan", 1000)
    dk.greet()

    adk = Akudaikan("akudaikan", 1000)
    adk.get_sodenosita(500)
    adk.greet()

    adk.get_sodenosita(500)
    adk.greet()
