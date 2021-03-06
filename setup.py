# coding: utf-8

"""
    API Definitions for RainMaker Backend Service

    This Swagger file provides the details about the RainMaker platform APIs.<br><br> There are two types of APIs supported by RainMaker - Unauthenticated and Authenticated.<br> The authenticated APIs are marked in the Swagger file, with a “lock” sign in front of them.<br> For the Unauthenticated APIs, there is no need to provide any authentication tokens in the HTTP header.<br> When the user logs in successfully, he receives access_token in the response. For the Authenticated APIs, this access_token needs to be passed in the \"Authorization\" HTTP header as the authentication token.<br> <br> <b>Note:</b><br><ul><li>RainMaker APIs do not support using double slashes after the resources or methods. Including a double slash goes against HTTP best practices. <br><li>The RainMaker APIs do not support following HTTP headers - data, verify and cookies.</ul>  # noqa: E501

    OpenAPI spec version: 1.1.17-fd1c887_2022-05-24T06:46
    Contact: esp-rainmaker-admin@espressif.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "rainmaker-api-client"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="API Definitions for RainMaker Backend Service",
    author_email="esp-rainmaker-admin@espressif.com",
    url="",
    keywords=["Swagger", "API Definitions for RainMaker Backend Service"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    This Swagger file provides the details about the RainMaker platform APIs.&lt;br&gt;&lt;br&gt; There are two types of APIs supported by RainMaker - Unauthenticated and Authenticated.&lt;br&gt; The authenticated APIs are marked in the Swagger file, with a “lock” sign in front of them.&lt;br&gt; For the Unauthenticated APIs, there is no need to provide any authentication tokens in the HTTP header.&lt;br&gt; When the user logs in successfully, he receives access_token in the response. For the Authenticated APIs, this access_token needs to be passed in the \&quot;Authorization\&quot; HTTP header as the authentication token.&lt;br&gt; &lt;br&gt; &lt;b&gt;Note:&lt;/b&gt;&lt;br&gt;&lt;ul&gt;&lt;li&gt;RainMaker APIs do not support using double slashes after the resources or methods. Including a double slash goes against HTTP best practices. &lt;br&gt;&lt;li&gt;The RainMaker APIs do not support following HTTP headers - data, verify and cookies.&lt;/ul&gt;  # noqa: E501
    """
)
