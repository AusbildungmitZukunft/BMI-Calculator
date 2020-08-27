# BMI Rechner
# erstellt von AusbildungmitZukunft
import locale
locale.setlocale(locale.LC_ALL,'de_DE')
print("\tBMI Rechner")
höhe = input("Bitte gib dein Größe ein\n")
größe = locale.atof( höhe )
gewicht = int(input("Bitte gib dein Gewicht ein\n"))
bmi = (gewicht/(größe*größe))

if bmi <= 18.5:
      print("Dein BMI ist", bmi,"du bist untergewichtig.")
elif 18.5 > bmi < 25:
      print("Dein BMI ist", bmi,"Du bist normal Gewichtig.")
elif 25 > bmi < 30:
      print("Dein BMI ist", bmi,"Du bist übergewichtig.")
elif bmi > 30:
      print("Dein BMI ist", bmi,"Du bist Fettleibig.")

else:
    print("Ein fehler ist aufgetreten bei deiner eingabe")
    print("Bitte überprüfe ob du eine ganze Zahl eingegeben hast\n")