# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01

if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://soniya709: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@github.com/soniya709/SoniyaXFilter.git /SoniyaXFilter 
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /SoniyaXFilter 
fi
cd /SoniyaXFilter 
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
