import time
from py_stealth import *


class VendorSearch:
    def __init__(self):
        for _x in range(0, 3):
            for _i in range(0, GetGumpsCount()):
                CloseSimpleGump(_i)
                Wait(250)
        RequestContextMenu(Self())
        Wait(250)
        SetContextMenuHook(0, 0)
        _test = GetContextMenu().splitlines()
        _i = 0
        for _string in _test:
            if "Vendor Search" not in _string:
                _i += 1
            else:
                SetContextMenuHook(Self(), _i)
                RequestContextMenu(Self())
        ClearContextMenu()
        SetContextMenuHook(0, 0)
        Wait(250)
        NumGumpButton(0, 2)
        Wait(250)

    def Search(self):
        Wait(250)
        NumGumpButton(0, 1)
        Wait(250)
        _searching = True
        _success = False
        _timeout = time.time() + 60*2  # 2 minutes from now
        while _searching:
            for _i in range(0, GetGumpsCount()):
                if GetGumpID(_i) == 999113:
                    _searching = False
                    _success = True
                    break
                elif time.time() > _timeout:
                    _searching = False
                    _success = False
                    break
                elif GetGumpID(_i) == 999115:
                    print("waiting")
                    Wait(250)
        return _success

    def Results(self):
        _resultsGumpIndex = 0
        _results = ""
        _result = []
        _response = []
        for _i in range(0, GetGumpsCount()):
            if GetGumpID(_i) == 999113:
                _resultsGumpIndex = _i
        _results = GetGumpInfo(_resultsGumpIndex)
        _results = _results['Tooltips']
        for _param in _results:
            if _param['ClilocID'] in range(1151488, 1151496):
                continue
            _result.append(_param['Arguments'])
            if _param['ClilocID'] == 1060639:
                _response.append(_result)
                _result = []
        return _response

    def DiscordSearch(self, _params):
        _params = _params.replace(" ", "")
        _params = _params.split(',')
        for _param in _params:
            if _param.startswith("di:"):
                self.DamageIncrease(_param[3:])
            elif _param.startswith("ssi:"):
                self.SSI(_param[4:])
            elif _param.startswith("ep:"):
                self.EP(_param[3:])
            elif _param.startswith("hci:"):
                self.HCI(_param[4:])
            elif _param.startswith("dci:"):
                self.DCI(_param[4:])
            elif _param.startswith("fcr:"):
                self.FCR(_param[4:])
            elif _param.startswith("fc:"):
                self.FC(_param[3:])
            elif _param.startswith("lrc:"):
                self.LRC(_param[4:])
            elif _param.startswith("lmc:"):
                self.LMC(_param[4:])
            elif _param.startswith("sort:"):
                self.Sort(_param[5:])
            elif _param.startswith("garg:"):
                self.Garg(_param[5:])
            elif _param.startswith("elf:"):
                self.Elf(_param[4:])
            elif _param.startswith("splinter:"):
                self.Splintering(_param[9:])
            elif _param.startswith("physdmg:"):
                self.PhysicalDamage(_param[5:])
            elif _param.startswith("fdmg:"):
                self.FireDamage(_param[5:])
            elif _param.startswith("cdmg:"):
                self.ColdDamage(_param[5:])
            elif _param.startswith("pdmg:"):
                self.PoisonDamage(_param[5:])
            elif _param.startswith("edmg:"):
                self.EnergyDamage(_param[5:])
            elif _param.startswith("cursed:"):
                self.Cursed(_param[5:])
        return self.Search()

    def DamageIncrease(self, _value):
        NumGumpTextEntry(0, 10, str(_value))
        Wait(250)
        NumGumpButton(0, 67)
        Wait(250)

    def DCI(self, _value):
        NumGumpTextEntry(0, 11, str(_value))
        Wait(250)
        NumGumpButton(0, 68)
        Wait(250)

    def HCI(self, _value):
        NumGumpTextEntry(0, 12, str(_value))
        Wait(250)
        NumGumpButton(0, 69)
        Wait(250)

    def SSI(self, _value):
        NumGumpTextEntry(0, 13, str(_value))
        Wait(250)
        NumGumpButton(0, 70)
        Wait(250)

    def SoulCharge(self, _value):
        NumGumpTextEntry(0, 14, str(_value))
        Wait(250)
        NumGumpButton(0, 71)
        Wait(250)

    def FireEater(self, _value):
        NumGumpTextEntry(0, 15, str(_value))
        Wait(250)
        NumGumpButton(0, 80)
        Wait(250)

    def ColdEater(self, _value):
        NumGumpTextEntry(0, 16, str(_value))
        Wait(250)
        NumGumpButton(0, 16)
        Wait(250)

    def PoisonEater(self, _value):
        NumGumpTextEntry(0, 17, str(_value))
        Wait(250)
        NumGumpButton(0, 82)
        Wait(250)

    def EnergyEater(self, _value):
        NumGumpTextEntry(0, 18, str(_value))
        Wait(250)
        NumGumpButton(0, 83)
        Wait(250)

    def KineticEater(self, _value):
        NumGumpTextEntry(0, 19, str(_value))
        Wait(250)
        NumGumpButton(0, 84)
        Wait(250)

    def DamageEater(self, _value):
        NumGumpTextEntry(0, 20, str(_value))
        Wait(250)
        NumGumpButton(0, 85)
        Wait(250)

    def FireResonance(self, _value):
        NumGumpTextEntry(0, 21, str(_value))
        Wait(250)
        NumGumpButton(0, 86)
        Wait(250)

    def ColdResonance(self, _value):
        NumGumpTextEntry(0, 22, str(_value))
        Wait(250)
        NumGumpButton(0, 87)
        Wait(250)

    def PoisonResonance(self, _value):
        NumGumpTextEntry(0, 23, str(_value))
        Wait(250)
        NumGumpButton(0, 88)
        Wait(250)

    def EnergyResonance(self, _value):
        NumGumpTextEntry(0, 24, str(_value))
        Wait(250)
        NumGumpButton(0, 89)
        Wait(250)

    def KineticResonance(self, _value):
        NumGumpTextEntry(0, 25, str(_value))
        Wait(250)
        NumGumpButton(0, 90)
        Wait(250)

    def SDI(self, _value):
        NumGumpTextEntry(0, 26, str(_value))
        Wait(250)
        NumGumpButton(0, 91)
        Wait(250)

    def CF(self, _value):
        NumGumpTextEntry(0, 27, str(_value))
        Wait(250)
        NumGumpButton(0, 92)
        Wait(250)

    def FCR(self, _value):
        NumGumpTextEntry(0, 28, str(_value))
        Wait(250)
        NumGumpButton(0, 93)
        Wait(250)

    def FC(self, _value):
        NumGumpTextEntry(0, 29, str(_value))
        Wait(250)
        NumGumpButton(0, 94)
        Wait(250)

    def LMC(self, _value):
        NumGumpTextEntry(0, 30, str(_value))
        Wait(250)
        NumGumpButton(0, 95)
        Wait(250)

    def LRC(self, _value):
        NumGumpTextEntry(0, 31, str(_value))
        Wait(250)
        NumGumpButton(0, 96)
        Wait(250)

    def MageWeapon(self, _value):
        NumGumpTextEntry(0, 32, str(_value))
        Wait(250)
        NumGumpButton(0, 97)
        Wait(250)

    def EP(self, _value):
        NumGumpTextEntry(0, 33, str(_value))
        Wait(250)
        NumGumpButton(0, 116)
        Wait(250)

    def Luck(self, _value):
        NumGumpTextEntry(0, 35, str(_value))
        Wait(250)
        NumGumpButton(0, 118)
        Wait(250)

    def RPD(self, _value):
        NumGumpTextEntry(0, 36, str(_value))
        Wait(250)
        NumGumpButton(0, 119)
        Wait(250)

    def SelfRepair(self, _value):
        NumGumpTextEntry(0, 37, str(_value))
        Wait(250)
        NumGumpButton(0, 120)
        Wait(250)

    def Rarity(self, _value):
        NumGumpTextEntry(0, 38, str(_value))
        Wait(250)
        NumGumpButton(0, 121)
        Wait(250)

    def PhysicalDamage(self, _value):
        NumGumpTextEntry(0, 39, str(_value))
        Wait(250)
        NumGumpButton(0, 122)
        Wait(250)

    def ColdDamage(self, _value):
        NumGumpTextEntry(0, 40, str(_value))
        Wait(250)
        NumGumpButton(0, 123)
        Wait(250)

    def FireDamage(self, _value):
        NumGumpTextEntry(0, 41, str(_value))
        Wait(250)
        NumGumpButton(0, 124)
        Wait(250)

    def PoisonDamage(self, _value):
        NumGumpTextEntry(0, 42, str(_value))
        Wait(250)
        NumGumpButton(0, 125)
        Wait(250)

    def EnergyDamage(self, _value):
        NumGumpTextEntry(0, 43, str(_value))
        Wait(250)
        NumGumpButton(0, 126)
        Wait(250)

    def Sort(self, _value):
        if _value == "high":
            NumGumpButton(0, 237)
            Wait(250)
        elif _value == "low":
            NumGumpButton(0, 236)
            Wait(250)

    def Antique(self, _value):
        if _value:
            NumGumpButton(0, 114)
            Wait(250)
        else:
            NumGumpButton(0, 115)
            Wait(250)

    def Brittle(self, _value):
        if _value:
            NumGumpButton(0, 112)
            Wait(250)
        else:
            NumGumpButton(0, 113)
            Wait(250)

    def Cursed(self, _value):
        if _value:
            NumGumpButton(0, 108)
            Wait(250)
        else:
            NumGumpButton(0, 109)
            Wait(250)

    def Garg(self, _value):
        if _value:
            NumGumpButton(0, 101)
            Wait(250)
        else:
            NumGumpButton(0, 102)
            Wait(250)

    def Elf(self, _value):
        if _value:
            NumGumpButton(0, 103)
            Wait(250)
        else:
            NumGumpButton(0, 104)
            Wait(250)

    def Splintering(self, _value):
        NumGumpTextEntry(0, 43, str(_value))
        Wait(250)
        NumGumpButton(0, 126)
        Wait(250)




