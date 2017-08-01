import numpy as np
import pandas as pd


class MLUtility(object):

    def __init__(self, skewed_features):
        self.features_transformed = {}
        self.skewed_features = skewed_features
        self.features_transf_list = ['symboling', 'normalized-losses', 'wheel-base',
        'length', 'width', 'height', 'curb-weight', 'engine-size', 'bore', 'stroke',
        'compression-ratio', 'horsepower', 'peak-rpm', 'city-mpg', 'highway-mpg',
        'make_audi', 'make_bmw', 'make_chevrolet', 'make_dodge', 'make_honda',
        'make_jaguar', 'make_mazda', 'make_mercedes-benz', 'make_mitsubishi',
        'make_nissan', 'make_peugot', 'make_plymouth', 'make_porsche', 'make_saab',
        'make_subaru', 'make_toyota', 'make_volkswagen', 'make_volvo', 'fuel-type_diesel',
        'fuel-type_gas', 'aspiration_std', 'aspiration_turbo', 'num-of-doors_four',
        'num-of-doors_two', 'body-style_convertible', 'body-style_hardtop',
        'body-style_hatchback', 'body-style_sedan', 'body-style_wagon',
        'drive-wheels_4wd', 'drive-wheels_fwd', 'drive-wheels_rwd',
        'engine-location_front', 'engine-type_dohc', 'engine-type_l',
        'engine-type_ohc', 'engine-type_ohcf', 'engine-type_ohcv',
        'num-of-cylinders_eight', 'num-of-cylinders_five', 'num-of-cylinders_four',
        'num-of-cylinders_six', 'num-of-cylinders_three', 'fuel-system_1bbl',
        'fuel-system_2bbl', 'fuel-system_idi', 'fuel-system_mfi',
        'fuel-system_mpfi', 'fuel-system_spdi']

        self.dataset = pd.read_csv('../Automobile_data.csv')

        for feature in self.features_transf_list:
            self.features_transformed[feature] = 0.0


    def parse_features(self,features_dict):
        for key, value in features_dict.iteritems():
            if type(value) is unicode:
                dict_key = key + '_' + value
                self.features_transformed[dict_key] = 1.0
            else:
                if key in self.skewed_features:
                    feature_max_val, feature_min_val = self.get_max_min_val(key)
                    log_transf_feature = np.log(value)
                    scaled_feature = self.scale_feature_value(log_transf_feature, feature_max_val, feature_min_val)
                    self.features_transformed[key] = scaled_feature
                else:
                    feature_max_val, feature_min_val = self.get_max_min_val(key)
                    scaled_feature = self.scale_feature_value(value, feature_max_val, feature_min_val)
                    self.features_transformed[key] = scaled_feature


        parsed_features_array = []

        for feature in self.features_transf_list:
            parsed_features_array.append(self.features_transformed[feature])

        return parsed_features_array


    def scale_feature_value(self,feature_value, max_val, min_val):
        print feature_value
        feature_std = (feature_value - min_val) / (max_val - min_val)
        return feature_std

    def get_max_min_val(self, feature):
        feature_data = self.dataset[feature]
        max_value = feature_data.max()
        min_value = feature_data.min()
        return max_value, min_value
