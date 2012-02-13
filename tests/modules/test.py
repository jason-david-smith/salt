# Import python libs
import os

# Import salt libs
import saltunittest

class TestModuleTest(saltunittest.ModuleCase):
    '''
    Validate the test module
    '''
    def test_ping(self):
        '''
        test.ping
        '''
        self.assertTrue(self.run_function('test.ping'))

    def test_echo(self):
        '''
        test.echo
        '''
        self.assertEqual(self.run_function('test.echo', ['text']), 'text')

    def test_version(self):
        '''
        test.version
        '''
        import salt
        self.assertEqual(self.run_function('test.version'), salt.__version__)

    def test_conf_test(self):
        '''
        test.conf_test
        '''
        self.assertEqual(self.run_function('test.conf_test'), 'baz')

    def test_get_opts(self):
        '''
        test.get_opts
        '''
        import salt.config
        opts = salt.config.minion_config(
                os.path.join(
                    saltunittest.TEST_DIR,
                    'files/conf/minion'
                    )
                )
        self.assertEqual(
                self.run_function('test.get_opts')['cachedir'],
                opts['cachedir']
                )

    def test_fib(self):
        '''
        test.fib
        '''
        self.assertEqual(
                self.run_function(
                    'test.fib',
                    ['40'],
                    )[0][-1],
                34
                )

    def test_collatz(self):
        '''
        test.collatz
        '''
        self.assertEqual(
                self.run_function(
                    'test.fib',
                    ['40'],
                    )[0][-1],
                34
                )

    def test_outputter(self):
        '''
        test.outputter
        '''
        self.assertEqual(self.run_function('test.outputter', ['text']), 'text')
