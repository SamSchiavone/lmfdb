import unittest

from flask import url_for
from lmfdb.tests import LmfdbTest

class PermalinkTest(LmfdbTest):

    """
    the following tests check if the url_for() actually gives
    what we expect
    """

    def ec(self):
        assert url_for('by_ec_label', label='17.a3') == '/EllipticCurve/Q/17.a3'


class RootTest(LmfdbTest):

    def test_root(self):
        root = self.tc.get("/")
        assert "database" in root.get_data(as_text=True)

    def test_robots(self):
        r = self.tc.get("/static/robots.txt")
        assert "Disallow: /static" in r.get_data(as_text=True)

    def test_favicon(self):
        assert len(self.tc.get("/favicon.ico").get_data()) > 10

    def test_javscript(self):
        js = self.tc.get("/static/lmfdb.js").get_data(as_text=True)
        # click handler def for knowls
        assert r"""$("body").on("click", "*[knowl]", debounce(knowl_handle,500, true));""" in js

    def test_css(self):
        css = self.tc.get("/style.css").get_data(as_text=True)
        # def for knowls:
        assert '*[knowl]' in css
        assert 'border-bottom: 1px dotted' in css

    @unittest.skip("Tests all url_maps, but fails at the moment because of other errors")
    def test_url_map(self):
        """

        """
        for rule in self.app.url_map.iter_rules():
            if "GET" in rule.methods:
                tc = self.app.test_client()
                res = tc.get(rule.rule)
                assert "Database" in res.get_data(as_text=True), "rule %s failed " % rule

    @unittest.skip("Tests for latex errors, but fails at the moment because of other errors")
    def test_some_latex_error(self):
        """
          Tests for latex errors, but fails at the moment because of other errors
        """
        for rule in self.app.url_map.iter_rules():
            if "GET" in rule.methods:
                try:
                    tc = self.app.test_client()
                    res = tc.get(rule.rule)
                    assert "Undefined control sequence" not in res.get_data(as_text=True), "rule %s failed" % rule
                except KeyError:
                    pass

    random_urls = ["/ModularForm/GL2/Q/Maass/"]
