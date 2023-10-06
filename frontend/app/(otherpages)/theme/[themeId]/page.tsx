import { fetchThemeDetail } from "@/utils";
import { ThemeStockList, ErrorComp } from "@/components";

import { NextPage } from "next";

interface themeId {
  themeId: string;
}
interface themeName {
  name: string;
}

interface ThemeDetailProps {
  params: themeId;
  searchParams: themeName;
}
const ThemeDetail: NextPage<ThemeDetailProps> = async ({
  params,
  searchParams,
}) => {
  const themeNumber = parseInt(params.themeId, 10);

  if (isNaN(themeNumber)) {
    return <ErrorComp />;
  } else {
    const stockList = await fetchThemeDetail(themeNumber);

    const stockIsEmpty =
      stockList === null ||
      !Array.isArray(stockList) ||
      stockList.length < 1 ||
      !stockList;

    if (stockIsEmpty) {
      return <ErrorComp />;
    } else {
      return (
        <div className="flex flex-col justify-between h-fit lg:flex-row">
          <div className="lg:w-1/3 bg-[#24364d] text-white">
            <div className="mt-40 mx-10">
              <h1 className="text-3xl font-bold mb-2">{searchParams.name}</h1>
              <h2 className="text-lg">
                {searchParams.name} 테마의 종목들을 보여드려요
              </h2>
            </div>
          </div>
          <div className="lg:w-2/3">
            {!stockIsEmpty ? (
              <div>
                <ThemeStockList stocks={stockList} />
              </div>
            ) : (
              <div>테마 혹은 이 테마에 해당하는 종목이 존재하지 않습니다.</div>
            )}
          </div>
        </div>
      );
    }
  }
};

export default ThemeDetail;
