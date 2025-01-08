import spade as sp

class DummyAgent(sp.agent.Agent):
    async def setup(self):
        print("Hello World! I'm agent {}".format(str(self.jid)))

async def main():
    dummy = DummyAgent("donjoshua@jabber.fr", "dinoserver")
    await dummy.start()

if __name__ == "__main__":
    sp.run(main())