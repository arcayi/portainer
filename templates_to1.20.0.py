# %%
# import pandas as pd
import json
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s\t%(levelname)s"
    "\t%(filename)s\t%(lineno)d\t%(funcName)s: "
    "%(message)s",
)


def main():
    temp_file_path = Path("templates.json")
    logging.debug("temp_file_path=%s", temp_file_path)

    json_temp = json.load(temp_file_path.open())
    # logging.debug("json_temp=\n%s", json.dumps(json_temp))

    # df_temp = pd.read_json(temp_file_path)
    # logging.debug("df_temp=\n%s", df_temp)
    # logging.debug("df_temp.to_json=\n%s", df_temp.to_json(orient='records'))
    map_trans = {"type": {"container": 1}}
    map_addkey = {"volumes": "container"}
    res = []
    for json_item in json_temp:
        logging.info("<json_item:\n%s", json_item)

        for k_map, v_map in map_trans.items():
            logging.debug("map_trans\tk_map=%s\tv_map=%s", k_map, v_map)
            if k_map in json_item.keys():
                for k1, v1 in v_map.items():
                    if k1 == json_item[k_map]:
                        json_item[k_map] = v1

        for k_map, v_map in map_addkey.items():
            logging.debug("map_addkey\tk_map=%s\tv_map=%s", k_map, v_map)
            if k_map in json_item.keys():
                json_item[k_map] = [
                    {v_map: v_json} for v_json in json_item[k_map]
                ]
                logging.info("!!!!map_addkey\tk_map=%s\tv_map=%s\njson_item[k_map]=%s", k_map, v_map,json_item[k_map])
        logging.info("<json_item:\n%s", json_item)
        res.append(json_item)
    logging.debug("res:\n%s", res)
    return res


if __name__ == "__main__":
    temp_file_path = Path("templates.json").with_name('templates.1.20.0.json')
    new_json = main()
    json.dump(new_json, temp_file_path.open(mode='wt'))
