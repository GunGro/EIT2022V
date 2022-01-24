import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from copy import copy


def _age_effect(age: int):
    """ tail sigmoid from a to b"""
    a = 0.2
    b = -0.1
    age = age - 16 # translate
    return a + (b-a) *(2 /(1+np.exp(-0.25*age)) - 1)
def _is_male_effect(is_male: bool):
    return 0.03 if is_male else -0.20
def _is_norwegain_effect(is_nor: bool):
    return 0.07 if is_nor else -0.02
def _do_study_in_norway_effect(in_nor: bool):
    return 0.15 if in_nor else -0.07
def _is_close_to_parents_effect(is_close: bool):
    return 1 if is_close else -0.7
def _annual_inc_effect(annual_inc: str):
    if annual_inc == "0 NOK":
        return 0.08
    if annual_inc == "0 - 20 000 NOK":
        return 0.09
    if annual_inc == "20 000 - 100 000 NOK":
        return 0.04
    if annual_inc == "100 000 - 195 000 NOK":
        return -0.06
    if annual_inc == "195 000 - 295 000 NOK":
        return -0.10
    if annual_inc == "Above 295 000 NOK":
        return 1
def _net_worth_effect(net_worth: str):
    if net_worth == "Below 0 NOK":
        return 0.02
    if net_worth == "0 - 100 000 NOK":
        return 0.01
    if net_worth == "100 000 - 400 000 NOK":
        return -0.03
    if net_worth == "Above 400 000 NOK":
        return 0.75
def _postal_code_effect(
    post_code: int,
    r=np.random.uniform(-0.02, 0.02, size= 10)
):
    if post_code == 0:
        return r[0]
    if post_code == 1000:
        return r[1]
    if post_code == 2000:
        return r[2]
    if post_code == 3000:
        return r[3]
    if post_code == 4000:
        return r[4]
    if post_code == 5000:
        return r[5]
    if post_code == 6000:
        return r[6]
    if post_code == 7000:
        return r[7]
    if post_code == 8000:
        return r[8]
    if post_code == 9000:
        return r[9]
def _study_deg_effect(deg: str):
    if deg == "Bachelor":
        return 0.1
    if deg == "Masters":
        return 0.05
    if deg == "PhD":
        return -0.03
def _study_subj_effect(subj: str, r = np.random.uniform(-0.01, 0.01, 5)):
    if subj == "Natural Sciences": 
        return r[0]
    if subj == "Economics": 
        return r[1]
    if subj == "Social Studies": 
        return r[2]
    if subj == "Engineering": 
        return r[3]
    if subj == "Philosophy":
        return r[4]
def _year_start_effect(
    start: int,
    r = np.random.uniform(-0.01, 0.01,15)
):
    start = start - 2015
    return 0.02 + 0.003 * start + r[start]
def _year_finish_effect(
    finish: int,
    r = np.random.uniform(-0.005, 0.005, 19)
):
    return r[finish - 2016]
def _uni_cred_effect(cred: str):
    if cred == "0-180":
        return 0.10
    if cred == "180-300":
        return 0.05
    if cred == "300+":
        return -0.08
def _tuition_fee_effect(
    fee: str,
    r = np.random.uniform(-0.01, 0.01, 3)
):
    if fee == "0 - 999 NOK":
        return r[0]
    if fee == "1000 - 10 000 NOK":
        return r[1]
    if fee == "Above 10 000 NOK":
        return r[2]
def _has_children_effect(has_children: bool):
    if has_children:
        return 0.03
    else:
        return -0.01

class DummyModel:
    base_line_odds = 0.25/0.75 # procent to be positive divided by percent to be negative

    age = {"x": [], "y": []}
    is_male = {"x": [], "y": []}
    is_norwegain = {"x": [], "y": []}
    do_study_in_norway = {"x": [], "y": []}
    is_close_to_parents = {"x": [], "y": []}
    annual_inc = {"x": [], "y": []}
    net_worth = {"x": [], "y": []}
    postal_code = {"x": [], "y": []}
    study_deg = {"x": [], "y": []}
    study_subj = {"x": [], "y": []}
    year_start = {"x": [], "y": []}
    year_finish = {"x": [], "y": []}
    uni_cred = {"x": [], "y": []}
    tuition_fee = {"x": [], "y": []}
    has_children = {"x": [], "y": []}
    # all true false variables
    for i in [True, False]:
        has_children["x"].append(i)
        has_children["y"].append(_has_children_effect(i))
        is_male["y"].append(_is_male_effect(i))
        is_male["x"].append(i)
        is_norwegain["y"].append(_is_norwegain_effect(i))
        is_norwegain["x"].append(i)
        do_study_in_norway["y"].append(_do_study_in_norway_effect(i))
        do_study_in_norway["x"].append(i)
        is_close_to_parents["y"].append(_is_close_to_parents_effect(i))
        is_close_to_parents["x"].append(i)
    for i in ["Bachelor", "Masters", "PhD"]:
        study_deg["y"].append(_study_deg_effect(i))
        study_deg["x"].append(i)
    for i in [
        "Natural Sciences",
        "Economics",
        "Social Studies",
        "Engineering",
        "Philosophy"
    ]:
        study_subj["y"].append(_study_subj_effect(i))
        study_subj["x"].append(i)
    for i in [
        "0 NOK",
        "0 - 20 000 NOK",
        "20 000 - 100 000 NOK",
        "100 000 - 195 000 NOK",
        "195 000 - 295 000 NOK",
        "Above 295 000 NOK"
    ]:
        annual_inc["y"].append(_annual_inc_effect(i))
        annual_inc["x"].append(i)
    for i in [
        "Below 0 NOK",
        "0 - 100 000 NOK",
        "100 000 - 400 000 NOK",
        "Above 400 000 NOK"
    ]:
        net_worth["y"].append(_net_worth_effect(i))
        net_worth["x"].append(i)
    for i in ["0-180", "180-300", "300+"]:
        uni_cred["y"].append(_uni_cred_effect(i))
        uni_cred["x"].append(i)
    for i in ["0 - 999 NOK", "1000 - 10 000 NOK", "Above 10 000 NOK"]:
        tuition_fee["y"].append(_tuition_fee_effect(i))
        tuition_fee["x"].append(i)
    for i in range(0, 10000, 1000):
        postal_code["y"].append(_postal_code_effect(i))
        postal_code["x"].append(i)
    for i in range(2015,2030):
        year_start["y"].append(_year_start_effect(i))
        year_start["x"].append(i)
    for i in range(2016,2035):
        year_finish["y"].append(_year_finish_effect(i))
        year_finish["x"].append(i)
    # age variable
    for i in range(16, 80):
        age["y"].append(_age_effect(i))
        age["x"].append(i)


    def _process_state_dict(self, state_dict):
        if "age" in state_dict:
            try:
                state_dict["age"] = int(state_dict["age"])
            except:
                state_dict["age"] = 18
        if "sex" in state_dict:
            state_dict["is_male"] = True if state_dict["sex"] == "Male" else False
        if "citizen" in state_dict:
            state_dict["is_norwegain"] = True if state_dict["citizen"] == "Norwegian" else False
        if "country" in state_dict:
            state_dict["do_study_in_norway"] = True if state_dict["country"] == "Norway" else False
        if "with_parent" in state_dict:
            state_dict["is_close_to_parents"] = state_dict["with_parent"]
        if "annual_inc" in state_dict:
            pass
        if "net_worth" in state_dict:
            pass
        if "postal" in state_dict:
            try:
                state_dict["post_code"] = int(float(state_dict["postal"])/1000)*1000
            except:
                state_dict["post_code"] = 0
        if "deg" in state_dict:
            state_dict["study_deg"] = state_dict["deg"]
        if "subj" in state_dict:
            state_dict["study_subj"] = state_dict["subj"]
        if "start" in state_dict:
            try:
                state_dict["year_start"] = int(state_dict["start"])
            except:
                state_dict["year_start"] = 2020
        if "finish" in state_dict:
            try:
                state_dict["year_finish"] = int(state_dict["finish"])
            except:
                state_dict["year_finish"] = 2021
        if "cred" in state_dict:
            state_dict["uni_cred"] = state_dict["cred"]
        if "fee" in state_dict:
            state_dict["tuition_fee"] = state_dict["fee"]
        if "is_parent" in state_dict:
            state_dict["has_children"] = state_dict["is_parent"]
        return state_dict




    def create_effects_image(self, state_dict = {}):
        fig, axes = plt.subplots(figsize = (20,15),  nrows = 3, ncols=5, sharey=True)

        pd.DataFrame(self.age).plot("x", "y", ax = axes[0,0], legend = False, title="Age", xlabel = '', fontsize = 12, color ="#410464")
        pd.DataFrame(self.is_male).plot.bar("x", "y", ax = axes[0,1], legend = False, title = "Sex", xlabel = '', fontsize = 12, color ="#410464")
        pd.DataFrame(self.is_norwegain).plot.bar("x", "y", ax = axes[0,2], legend = False, title = "Country Citizen", xlabel = '', fontsize = 12, color ="#410464")
        pd.DataFrame(self.do_study_in_norway).plot.bar("x", "y", ax = axes[0,3], legend = False, title = "Country Study", xlabel = '', fontsize = 12, color ="#410464")
        pd.DataFrame(self.is_close_to_parents).plot.bar("x", "y", ax = axes[0,4], legend = False, title = "Same Municipality as Parents", xlabel = '', fontsize = 12, color ="#410464")
        pd.DataFrame(self.annual_inc).plot.bar("x", "y", ax = axes[1,0], legend = False, title = "Annual Income", xlabel = '', fontsize = 12, color ="#410464")
        pd.DataFrame(self.net_worth).plot.bar("x", "y", ax = axes[1,1], legend = False, title = "Personal Assets", xlabel = '', fontsize = 12, color ="#410464")
        pd.DataFrame(self.postal_code).plot.bar("x", "y", ax = axes[1,2], legend = False, title = "Postal Code", xlabel = '', fontsize = 12, color ="#410464")
        pd.DataFrame(self.study_deg).plot.bar("x", "y", ax = axes[1,3], legend = False, title = "Study Degree", xlabel = '', fontsize = 12, color ="#410464")
        pd.DataFrame(self.study_subj).plot.bar("x", "y", ax = axes[1,4], legend = False, title = "Study Subject", xlabel = '', fontsize = 12, color ="#410464")
        pd.DataFrame(self.year_start).plot("x", "y", ax = axes[2,0], legend = False, title = "Year of Study Start", xlabel = '', fontsize = 12, color ="#410464")
        pd.DataFrame(self.year_finish).plot("x", "y", ax = axes[2,1], legend = False, title = "Year of Study Finsih", xlabel = '', fontsize = 12, color ="#410464")
        pd.DataFrame(self.uni_cred).plot.bar("x", "y", ax = axes[2,2], legend = False, title = "Univercity Credits", xlabel = '', fontsize = 12, color ="#410464")
        pd.DataFrame(self.tuition_fee).plot.bar("x", "y", ax = axes[2,3], legend = False, title = "Tuition Fee", xlabel = '', fontsize = 12, color ="#410464")
        pd.DataFrame(self.has_children).plot.bar("x", "y", ax = axes[2,4], legend = False, title = "Is a Parent", xlabel = '', fontsize = 12, color ="#410464")
        for ax in axes.ravel():
            ax.set_facecolor("#F4F4F4")
            ax.set_xticklabels([])
        if state_dict:
            state_dict = self._process_state_dict(state_dict)
            axes[0,0].axvline(x = state_dict["age"], color = "red")
            axes[0,1].axvline(x = not state_dict["is_male"], color = "red")
            axes[0,2].axvline(x = not state_dict["is_norwegain"], color = "red")
            axes[0,3].axvline(x = not state_dict["do_study_in_norway"], color = "red")
            axes[0,4].axvline(x = not state_dict["is_close_to_parents"], color = "red")

            axes[1,0].axvline(x = self.annual_inc["x"].index(state_dict["annual_inc"]), color = "red")
            axes[1,1].axvline(x = self.net_worth["x"].index(state_dict["net_worth"]), color = "red")
            axes[1,2].axvline(x = state_dict["post_code"]//1000, color = "red")
            axes[1,3].axvline(x = self.study_deg["x"].index(state_dict["study_deg"]), color = "red")
            axes[1,4].axvline(x = self.study_subj["x"].index(state_dict["study_subj"]), color = "red")
            axes[2,0].axvline(x = state_dict["year_start"], color = "red")
            axes[2,1].axvline(x = state_dict["year_finish"], color = "red")
            axes[2,2].axvline(x = self.uni_cred["x"].index(state_dict["uni_cred"]), color = "red")
            axes[2,3].axvline(x = self.tuition_fee["x"].index(state_dict["tuition_fee"]), color = "red")
            axes[2,4].axvline(x = not state_dict["has_children"], color = "red")
        return fig


    def get_model_output(self, state_dict):
        state_dict = self._process_state_dict(state_dict)
        r = copy(self.base_line_odds)
        r *= 1 + _age_effect(state_dict["age"])
        r *= 1 + _is_male_effect(state_dict["is_male"])
        r *= 1 + _is_norwegain_effect(state_dict["is_norwegain"])
        r *= 1 + _do_study_in_norway_effect(state_dict["do_study_in_norway"])
        r *= 1 + _is_close_to_parents_effect(state_dict["is_close_to_parents"])
        r *= 1 + _annual_inc_effect(state_dict["annual_inc"])
        r *= 1 + _net_worth_effect(state_dict["net_worth"])
        r *= 1 + _postal_code_effect(state_dict["post_code"])
        r *= 1 + _study_deg_effect(state_dict["study_deg"])
        r *= 1 + _study_subj_effect(state_dict["study_subj"])
        r *= 1 + _year_start_effect(state_dict["year_start"])
        r *= 1 + _year_finish_effect(state_dict["year_finish"])
        r *= 1 + _uni_cred_effect(state_dict["uni_cred"])
        r *= 1 + _tuition_fee_effect(state_dict["tuition_fee"])
        r *= 1 + _has_children_effect(state_dict["has_children"])

        risk = r/(1+r) * 100
        return risk

if __name__ == "__main__":
    """ Test for the functionality of the model """
    model = DummyModel()
    fig = model.create_effects_image()
    plt.show()

