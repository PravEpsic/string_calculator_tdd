from src.stringcalculator import StringCalculator

def test_Multiply():
    # arrange
    mon_param = "3;4;1;1001"
    mon_resultat = 12  # La multiplication attendue est de 3 * 4 * 1 = 12
    # act
    produit = StringCalculator.Multiply(mon_param)
    # assert
    assert produit == mon_resultat
