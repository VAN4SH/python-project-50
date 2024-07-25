import json
from gendiff import generate_diff

file_path1_json = 'file1.json'
file_path2_json = 'file2.json'

expected_stylish = """{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}"""

expected_plain = """Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]"""

expected_json = '{"common": {"follow": {"status": "added", "value": false}, "setting1": {"status": "unchanged", "value": "Value 1"}, "setting2": {"status": "removed", "value": 200}, "setting3": {"status": "changed", "old_value": true, "new_value": null}, "setting4": {"status": "added", "value": "blah blah"}, "setting5": {"status": "added", "value": {"key5": "value5"}}, "setting6": {"status": "nested", "value": {"doge": {"status": "nested", "value": {"wow": {"status": "changed", "old_value": "", "new_value": "so much"}}}, "key": {"status": "unchanged", "value": "value"}, "ops": {"status": "added", "value": "vops"}}}}, "group1": {"baz": {"status": "changed", "old_value": "bas", "new_value": "bars"}, "foo": {"status": "unchanged", "value": "bar"}, "nest": {"status": "changed", "old_value": {"key": "value"}, "new_value": "str"}}, "group2": {"status": "removed", "value": {"abc": 12345, "deep": {"id": 45}}}, "group3": {"status": "added", "value": {"deep": {"id": {"number": 45}}, "fee": 100500}}}'

def test_generate_diff_stylish():
    assert generate_diff(file_path1_json, file_path2_json, 'stylish') == expected_stylish

def test_generate_diff_plain():
    assert generate_diff(file_path1_json, file_path2_json, 'plain') == expected_plain

def test_generate_diff_json():
    assert generate_diff(file_path1_json, file_path2_json, 'json') == expected_json

if __name__ == "__main__":
    test_generate_diff_stylish()
    test_generate_diff_plain()
    test_generate_diff_json()
