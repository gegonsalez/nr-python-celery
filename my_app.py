import newrelic.agent
newrelic.agent.initialize('newrelic.ini')

from tasks import add, func_a, func_b

@newrelic.agent.background_task()
def using_nr_bg_decorator():
	result = add(3, 4)
	#newrelic.agent.add_custom_parameter('Add result', result)

def not_using_bg_decorator():
	result = add(5, 5)
	#newrelic.agent.add_custom_parameter('Add result', result)

if __name__ == "__main__":
	while True:
		using_nr_bg_decorator()
		not_using_bg_decorator()
		func_a()
		func_b()