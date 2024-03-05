from redbot.core.bot import Red

from .privatechannel import privatechannel


async def setup(bot: Red) -> None:
    await bot.add_cog(privatechannel(bot))
