from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import random

# Écran d'accueil (page 1)
class Page1(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        layout.add_widget(Label(text="Bienvenue dans mon logiciel !", font_size=32))
        btn_menu = Button(text="Menu Principal", size_hint=(None, None), size=(200, 50), pos_hint={'center_x': 0.5})
        btn_menu.bind(on_press=lambda x: setattr(self.manager, 'current', 'page2'))
        layout.add_widget(btn_menu)
        self.add_widget(layout)

# Menu Principal (page 2)
class Page2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        layout.add_widget(Label(text="Menu Principal", font_size=28))

        btn_jeux = Button(text="Jeux", size_hint=(1, None), height=50)
        btn_jeux.bind(on_press=lambda x: setattr(self.manager, 'current', 'page4'))
        layout.add_widget(btn_jeux)

        btn_outils = Button(text="Outils", size_hint=(1, None), height=50)
        btn_outils.bind(on_press=lambda x: setattr(self.manager, 'current', 'page5'))
        layout.add_widget(btn_outils)

        btn_info = Button(text="Information", size_hint=(1, None), height=50)
        btn_info.bind(on_press=lambda x: setattr(self.manager, 'current', 'page3'))
        layout.add_widget(btn_info)

        self.add_widget(layout)

# Page Information (page 3)
class Page3(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        layout.add_widget(Label(text="Information", font_size=28))
        layout.add_widget(Label(text="Logiciel en maintenance...", font_size=18))
        btn_retour = Button(text="Retour", size_hint=(None, None), size=(150, 50), pos_hint={'center_x': 0.5})
        btn_retour.bind(on_press=lambda x: setattr(self.manager, 'current', 'page2'))
        layout.add_widget(btn_retour)
        self.add_widget(layout)

# Page Jeux (page 4)
class Page4(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        layout.add_widget(Label(text="Jeux", font_size=28))

        btn_devine = Button(text="🎯 Devine le nombre", size_hint=(1, None), height=50)
        btn_devine.bind(on_press=lambda x: setattr(self.manager, 'current', 'page_devine'))
        layout.add_widget(btn_devine)

        btn_retour = Button(text="Retour", size_hint=(None, None), size=(150, 50), pos_hint={'center_x': 0.5})
        btn_retour.bind(on_press=lambda x: setattr(self.manager, 'current', 'page2'))
        layout.add_widget(btn_retour)

        self.add_widget(layout)

# Jeu Devine le nombre
class PageDevine(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.nombre_secret = random.randint(1, 100)
        self.essais = 0
        self.limite_essais = 15

        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=15)

        self.label_info = Label(text="🎯 Devine un nombre entre 1 et 100", font_size=24)
        self.layout.add_widget(self.label_info)

        self.input_nombre = TextInput(multiline=False, input_filter='int', size_hint=(None, None), size=(200, 40), halign="center")
        self.layout.add_widget(self.input_nombre)

        btn_verifier = Button(text="Vérifier", size_hint=(None, None), size=(150, 50))
        btn_verifier.bind(on_press=self.verifier_nombre)
        self.layout.add_widget(btn_verifier)

        btn_nouvelle = Button(text="Nouvelle partie", size_hint=(None, None), size=(150, 50))
        btn_nouvelle.bind(on_press=self.nouvelle_partie)
        self.layout.add_widget(btn_nouvelle)

        btn_retour = Button(text="Retour", size_hint=(None, None), size=(150, 50))
        btn_retour.bind(on_press=lambda x: setattr(self.manager, 'current', 'page4'))
        self.layout.add_widget(btn_retour)

        self.add_widget(self.layout)

    def verifier_nombre(self, instance):
        try:
            guess = int(self.input_nombre.text)
        except ValueError:
            self.label_info.text = "⚠️ Entre un nombre valide."
            return

        self.essais += 1
        if guess == self.nombre_secret:
            self.label_info.text = f"🎉 Bravo ! Trouvé en {self.essais} essais."
        elif self.essais >= self.limite_essais:
            self.label_info.text = f"😢 Perdu ! Le nombre était {self.nombre_secret}."
        elif guess < self.nombre_secret:
            self.label_info.text = "C'est plus grand ⬆️"
        else:
            self.label_info.text = "C'est plus petit ⬇️"

        self.input_nombre.text = ""

    def nouvelle_partie(self, instance):
        self.nombre_secret = random.randint(1, 100)
        self.essais = 0
        self.label_info.text = "🎯 Devine un nombre entre 1 et 100"
        self.input_nombre.text = ""

# Page Outils (page 5)
class Page5(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        layout.add_widget(Label(text="Outils", font_size=28))

        btn_addition = Button(text="🧮 Addition", size_hint=(1, None), height=50)
        btn_addition.bind(on_press=lambda x: setattr(self.manager, 'current', 'page_addition'))
        layout.add_widget(btn_addition)

        btn_retour = Button(text="Retour", size_hint=(None, None), size=(150, 50), pos_hint={'center_x': 0.5})
        btn_retour.bind(on_press=lambda x: setattr(self.manager, 'current', 'page2'))
        layout.add_widget(btn_retour)

        self.add_widget(layout)

# Page Addition
class PageAddition(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=15)

        self.layout.add_widget(Label(text="🧮 Calculatrice Addition", font_size=24))

        self.entree_a = TextInput(multiline=False, input_filter='int', size_hint=(None, None), size=(200, 40))
        self.layout.add_widget(self.entree_a)

        self.entree_b = TextInput(multiline=False, input_filter='int', size_hint=(None, None), size=(200, 40))
        self.layout.add_widget(self.entree_b)

        btn_calculer = Button(text="Calculer", size_hint=(None, None), size=(150, 50))
        btn_calculer.bind(on_press=self.calculer_addition)
        self.layout.add_widget(btn_calculer)

        self.resultat_label = Label(text="", font_size=20)
        self.layout.add_widget(self.resultat_label)

        btn_retour = Button(text="Retour", size_hint=(None, None), size=(150, 50))
        btn_retour.bind(on_press=lambda x: setattr(self.manager, 'current', 'page5'))
        self.layout.add_widget(btn_retour)

        self.add_widget(self.layout)

    def calculer_addition(self, instance):
        try:
            a = int(self.entree_a.text)
            b = int(self.entree_b.text)
            self.resultat_label.text = f"Résultat : {a + b}"
        except ValueError:
            self.resultat_label.text = "⚠️ Entrez des nombres valides"

# Application principale
class MonApp(App):
    def build(self):
        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(Page1(name='page1'))
        sm.add_widget(Page2(name='page2'))
        sm.add_widget(Page3(name='page3'))
        sm.add_widget(Page4(name='page4'))
        sm.add_widget(PageDevine(name='page_devine'))
        sm.add_widget(Page5(name='page5'))
        sm.add_widget(PageAddition(name='page_addition'))
        sm.current = 'page1'  # Page de départ
        return sm

if __name__ == '__main__':
    MonApp().run()
