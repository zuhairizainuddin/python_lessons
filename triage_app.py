from PySide6 import QtWidgets


class MainWindow(QtWidgets.QWidget):
    # initialize the window
    def __init__(self):
        super().__init__()
        self.init_ui()

    # initialize ui
    def init_ui(self):
        self.setWindowTitle('TRIAGE APP')

        # Labels and line edits
        self.label_hr = QtWidgets.QLabel('Enter the heart rate (bpm):')
        self.hr_edit_line = QtWidgets.QLineEdit()
        self.label_sbp = QtWidgets.QLabel('Enter the SBP (mm/Hg):')
        self.sbp_edit_line = QtWidgets.QLineEdit()
        self.label_dbp = QtWidgets.QLabel('Enter the DBP (mm/Hg):')
        self.dbp_edit_line = QtWidgets.QLineEdit()
        self.label_rr = QtWidgets.QLabel('Enter the respiratory rate (bpm):')
        self.rr_edit_line = QtWidgets.QLineEdit()
        self.label_temp = QtWidgets.QLabel('Enter the temperature (Celcius):')
        self.temp_edit_line = QtWidgets.QLineEdit()
        self.label_spo = QtWidgets.QLabel('Enter the SPO2:')
        self.spo_edit_line = QtWidgets.QLineEdit()

        self.triage_label = QtWidgets.QLabel()

        self.label_avpu = QtWidgets.QLabel('AVPU score:')
        self.combo_avpu = QtWidgets.QComboBox()
        self.combo_avpu.addItem('A - Alert')
        self.combo_avpu.addItem('V - Responds to voice')
        self.combo_avpu.addItem('P - Responds to pain')
        self.combo_avpu.addItem('U - Unresponsive')

        # Create the calculate button
        self.button_triage = QtWidgets.QPushButton('Calculate Risk')
        self.button_triage.clicked.connect(self.calculate_triage)

        # Arrange the layout
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.label_hr)
        layout.addWidget(self.hr_edit_line)
        layout.addWidget(self.label_sbp)
        layout.addWidget(self.sbp_edit_line)
        layout.addWidget(self.label_dbp)
        layout.addWidget(self.dbp_edit_line)
        layout.addWidget(self.label_rr)
        layout.addWidget(self.rr_edit_line)
        layout.addWidget(self.label_temp)
        layout.addWidget(self.temp_edit_line)
        layout.addWidget(self.label_spo)
        layout.addWidget(self.spo_edit_line)
        layout.addWidget(self.label_avpu)
        layout.addWidget(self.combo_avpu)
        layout.addWidget(self.button_triage)
        layout.addWidget(self.triage_label)

        self.setLayout(layout)

    def calculate_triage(self):
        # get the values
        hr = int(self.hr_edit_line.text())
        sbp = int(self.sbp_edit_line.text())
        dbp = int(self.dbp_edit_line.text())
        rr = int(self.rr_edit_line.text())
        temp = int(self.temp_edit_line.text())
        spo = int(self.spo_edit_line.text())

        # Get AVPU score
        avpu = self.combo_avpu.currentText()

        hr_isabnormal = hr < 60 or hr > 100
        sbp_isabnormal = sbp < 90 or sbp > 140
        dbp_isabnormal = dbp < 60 or dbp > 90
        rr_isabnormal = rr < 12 or rr > 20
        temp_isabormal = temp < 35 or temp > 38
        spo_isabnormal = spo < 95

        vitals = [hr_isabnormal, sbp_isabnormal, dbp_isabnormal,
                  rr_isabnormal, temp_isabormal, spo_isabnormal]

        if vitals.count(True) == 6 or avpu == 'U - Unresponsive':
            triage_category = 'Very High Risk'
        elif vitals.count(True) > 1 or avpu == 'P - Responds to pain':
            triage_category = 'High Risk'
        elif vitals.count(True) == 1 or avpu == 'V - Responds to voice':
            triage_category = 'Medium Risk'
        else:
            triage_category = 'Low Risk'

        self.triage_label.setText(triage_category)


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    window = MainWindow()
    window.show()
    app.exec()
