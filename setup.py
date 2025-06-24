from distutils.core import setup

setup(
    name="Slowloris",
    py_modules=["slowloris"],
    entry_points={"console_scripts": ["slowloris=slowloris:main"]},
    version="0.2.6",
    description="Low bandwidth DoS tool. Slowloris rewrite in Python.",
    url="https://github.com/0x31i/slowloris",
    keywords=["dos", "http", "slowloris"],
    license="MIT",
)
