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
        #_test = GetContextMenu().splitlines()
        #_i = 0
        #for _string in _test:
            #if "Vendor Search" not in _string:
                #_i += 1
            #else:
                #SetContextMenuHook(Self(), _i)
                #RequestContextMenu(Self())
        SetContextMenuHook(Self(), 1)
        #RequestContextMenu(Self())
        #ClearContextMenu()
        Wait(250)
        SetContextMenuHook(0, 0)
        Wait(250)
        NumGumpButton(0, 2)
        Wait(250)
        print('VS Initialized')

    def Search(self):
        Wait(250)
        NumGumpButton(0, 1)
        Wait(250)
        _searching = True
        _success = False
        _timeout = time.time() + 60  # 1 minute from now
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
        _paging = True
        _button = 0
        while _paging:
            _paging = False
            _gumpSearching = True
            while _gumpSearching:
                for _i in range(0, GetGumpsCount()):
                    if GetGumpID(_i) == 999113:
                        _resultsGumpIndex = _i
                        _gumpSearching = False
                        break
                    else:
                        Wait(250)
                Wait(250)
            _results = GetGumpInfo(_resultsGumpIndex)
            _tooltips = _results['Tooltips']
            _htmltoks = _results['XmfHTMLTok']
            _gumpButtons = _results['GumpButtons']
            for _gumpButton in _gumpButtons:
                if _gumpButton['ElemNum'] == 6:
                    _button = _gumpButton['ReturnValue']
            for _htmltok in _htmltoks:
                if _htmltok['ClilocID'] == 1114514:
                    _paging = True
                    if "Higher" in _htmltok['Arguments']:
                        _paging = False
            for _param in _tooltips:
                if _param['ClilocID'] in range(1151488, 1151496):
                    continue
                _result.append(_param['ClilocText'])
                if _param['ClilocID'] == 1060639:
                    _response.append(_result)
                    _result = []
            if _paging:
                NumGumpButton(_resultsGumpIndex, _button)
                _gumpSearching = True
                while _gumpSearching:
                    for _i in range(0, GetGumpsCount()):
                        if GetGumpID(_i) == 999113:
                            _gumpSearching = False
                            break
                        else:
                            Wait(250)
                    Wait(250)
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
            elif _param.startswith("sdi:"):
                self.SDI(_param[4:])
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
            elif _param.startswith("manar:"):
                self.ManaRegen(_param[6:])
            elif _param.startswith("swords:"):
                self.Swords(_param[7:])
            elif _param.startswith("fencing:"):
                self.Fencing(_param[8:])
            elif _param.startswith("mace:"):
                self.Mace(_param[5:])
            elif _param.startswith("magery:"):
                self.Magery(_param[7:])
            elif _param.startswith("music:"):
                self.Music(_param[6:])
            elif _param.startswith("wrestling:"):
                self.Wrestling(_param[10:])
            elif _param.startswith("tactics:"):
                self.Tactics(_param[8:])
            elif _param.startswith("taming:"):
                self.Taming(_param[7:])
            elif _param.startswith("provo:"):
                self.Provo(_param[6:])
            elif _param.startswith("ss:"):
                self.SpiritSpeak(_param[3:])
            elif _param.startswith("stealth:"):
                self.Stealth(_param[8:])
            elif _param.startswith("parry:"):
                self.Parry(_param[6:])
            elif _param.startswith("med:"):
                self.Meditation(_param[4:])
            elif _param.startswith("lore:"):
                self.AnimalLore(_param[5:])
            elif _param.startswith("disco:"):
                self.Discord(_param[6:])
            elif _param.startswith("focus:"):
                self.Focus(_param[6:])
            elif _param.startswith("stealing:"):
                self.Stealing(_param[9:])
            elif _param.startswith("anatomy:"):
                self.Anatomy(_param[8:])
            elif _param.startswith("eval:"):
                self.EvalInt(_param[5:])
            elif _param.startswith("vet:"):
                self.Vet(_param[4:])
            elif _param.startswith("necro:"):
                self.Necro(_param[6:])
            elif _param.startswith("bush:"):
                self.Bushido(_param[5:])
            elif _param.startswith("myst:"):
                self.Mystic(_param[5:])
            elif _param.startswith("healing:"):
                self.Healing(_param[8:])
            elif _param.startswith("resist:"):
                self.Resist(_param[7:])
            elif _param.startswith("peace:"):
                self.Peace(_param[6:])
            elif _param.startswith("archery:"):
                self.Archery(_param[8:])
            elif _param.startswith("chiv:"):
                self.Chiv(_param[5:])
            elif _param.startswith("ninjitsu:"):
                self.Ninjitsu(_param[9:])
            elif _param.startswith("throwing:"):
                self.Throwing(_param[9:])
            elif _param.startswith("lj:"):
                self.Lumberjacking(_param[3:])
            elif _param.startswith("snoop:"):
                self.Snooping(_param[6:])
            elif _param.startswith("mining:"):
                self.Mining(_param[7:])
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
        NumGumpButton(0, 203)
        Wait(250)

    def Swords(self, _value):
        NumGumpTextEntry(0, 78, str(_value))
        Wait(250)
        NumGumpButton(0, 203)
        Wait(250)

    def Fencing(self, _value):
        NumGumpTextEntry(0, 79, str(_value))
        Wait(250)
        NumGumpButton(0, 204)
        Wait(250)

    def Mace(self, _value):
        NumGumpTextEntry(0, 80, str(_value))
        Wait(250)
        NumGumpButton(0, 205)
        Wait(250)

    def Magery(self, _value):
        NumGumpTextEntry(0, 81, str(_value))
        Wait(250)
        NumGumpButton(0, 206)
        Wait(250)

    def Music(self, _value):
        NumGumpTextEntry(0, 82, str(_value))
        Wait(250)
        NumGumpButton(0, 207)
        Wait(250)

    def Wrestling(self, _value):
        NumGumpTextEntry(0, 83, str(_value))
        Wait(250)
        NumGumpButton(0, 208)
        Wait(250)

    def Tactics(self, _value):
        NumGumpTextEntry(0, 84, str(_value))
        Wait(250)
        NumGumpButton(0, 209)
        Wait(250)

    def Taming(self, _value):
        NumGumpTextEntry(0, 85, str(_value))
        Wait(250)
        NumGumpButton(0, 210)
        Wait(250)

    def Provo(self, _value):
        NumGumpTextEntry(0, 86, str(_value))
        Wait(250)
        NumGumpButton(0, 211)
        Wait(250)

    def SpiritSpeak(self, _value):
        NumGumpTextEntry(0, 87, str(_value))
        Wait(250)
        NumGumpButton(0, 212)
        Wait(250)

    def Stealth(self, _value):
        NumGumpTextEntry(0, 88, str(_value))
        Wait(250)
        NumGumpButton(0, 213)
        Wait(250)

    def Parry(self, _value):
        NumGumpTextEntry(0, 89, str(_value))
        Wait(250)
        NumGumpButton(0, 214)
        Wait(250)

    def Meditation(self, _value):
        NumGumpTextEntry(0, 90, str(_value))
        Wait(250)
        NumGumpButton(0, 215)
        Wait(250)

    def AnimalLore(self, _value):
        NumGumpTextEntry(0, 91, str(_value))
        Wait(250)
        NumGumpButton(0, 216)
        Wait(250)

    def Discord(self, _value):
        NumGumpTextEntry(0, 92, str(_value))
        Wait(250)
        NumGumpButton(0, 217)
        Wait(250)

    def Focus(self, _value):
        NumGumpTextEntry(0, 93, str(_value))
        Wait(250)
        NumGumpButton(0, 218)
        Wait(250)

    def Stealing(self, _value):
        NumGumpTextEntry(0, 94, str(_value))
        Wait(250)
        NumGumpButton(0, 219)
        Wait(250)

    def Anatomy(self, _value):
        NumGumpTextEntry(0, 95, str(_value))
        Wait(250)
        NumGumpButton(0, 220)
        Wait(250)

    def EvalInt(self, _value):
        NumGumpTextEntry(0, 96, str(_value))
        Wait(250)
        NumGumpButton(0, 221)
        Wait(250)

    def Vet(self, _value):
        NumGumpTextEntry(0, 97, str(_value))
        Wait(250)
        NumGumpButton(0, 222)
        Wait(250)

    def Necro(self, _value):
        NumGumpTextEntry(0, 98, str(_value))
        Wait(250)
        NumGumpButton(0, 223)
        Wait(250)

    def Bushido(self, _value):
        NumGumpTextEntry(0, 99, str(_value))
        Wait(250)
        NumGumpButton(0, 224)
        Wait(250)

    def Mystic(self, _value):
        NumGumpTextEntry(0, 100, str(_value))
        Wait(250)
        NumGumpButton(0, 225)
        Wait(250)

    def Healing(self, _value):
        NumGumpTextEntry(0, 101, str(_value))
        Wait(250)
        NumGumpButton(0, 226)
        Wait(250)

    def Resist(self, _value):
        NumGumpTextEntry(0, 102, str(_value))
        Wait(250)
        NumGumpButton(0, 227)
        Wait(250)

    def Peace(self, _value):
        NumGumpTextEntry(0, 103, str(_value))
        Wait(250)
        NumGumpButton(0, 228)
        Wait(250)

    def Archery(self, _value):
        NumGumpTextEntry(0, 104, str(_value))
        Wait(250)
        NumGumpButton(0, 229)
        Wait(250)

    def Chiv(self, _value):
        NumGumpTextEntry(0, 105, str(_value))
        Wait(250)
        NumGumpButton(0, 230)
        Wait(250)

    def Ninjitsu(self, _value):
        NumGumpTextEntry(0, 106, str(_value))
        Wait(250)
        NumGumpButton(0, 231)
        Wait(250)

    def Throwing(self, _value):
        NumGumpTextEntry(0, 107, str(_value))
        Wait(250)
        NumGumpButton(0, 232)
        Wait(250)

    def Lumberjacking(self, _value):
        NumGumpTextEntry(0, 108, str(_value))
        Wait(250)
        NumGumpButton(0, 233)
        Wait(250)

    def Snooping(self, _value):
        NumGumpTextEntry(0, 109, str(_value))
        Wait(250)
        NumGumpButton(0, 234)
        Wait(250)

    def Mining(self, _value):
        NumGumpTextEntry(0, 110, str(_value))
        Wait(250)
        NumGumpButton(0, 235)
        Wait(250)

    def ManaRegen(self, _value):
        NumGumpTextEntry(0, 77, str(_value))
        Wait(250)
        NumGumpButton(0, 197)
        Wait(250)





