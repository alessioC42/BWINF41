#include <iostream>
#include <vector>
#include <algorithm>
#include <chrono>

class P
{
public:
    std::vector<int> stack;
    std::vector<int> history;
    std::vector<int> initStack;

    P(std::vector<int> stack, std::vector<int> history = {}, std::vector<int> initStack = {})
    {
        this->stack = stack;
        this->history = history;
        if (history.empty())
            this->initStack = stack;
        else
            this->initStack = initStack;
    }

    void flip(int i)
    {
        std::vector<int> stack = this->stack;
        for (int j = 0; j < (i + 1) / 2; j++)
        {
            std::swap(stack[j], stack[i - j]);
        }
        this->history.push_back(i);
        stack.erase(stack.begin());
        this->stack = stack;
    }

    void printHistory()
    {
        std::cout << "-- init_len:" << this->initStack.size() << "; flip_operations:" << this->history.size() << " --\n";
        std::cout << "-- : ";
        for (int i : this->initStack)
        {
            std::cout << i << " ";
        }
        std::cout << "\n";
        P stack(this->initStack);
        for (int flipindex : this->history)
        {
            stack.flip(flipindex);
            std::cout << flipindex << " : ";
            for (int i : stack.stack)
            {
                std::cout << i << " ";
            }
            std::cout << "\n";
        }
        std::cout << "PUWE: " << this->history.size() << "\n";
    }

    bool isValid()
    {
        for (int i = 0; i < this->stack.size() - 1; i++)
        {
            if (this->stack[i] >= this->stack[i + 1])
                return false;
        }
        return true;
    }

    P copy()
    {
        return P(this->stack, this->history, this->initStack);
    }

    std::vector<int> getFlipIndexPoints()
    {
        std::vector<int> points(this->stack.size());
        for (int i = 0; i < points.size(); i++)
            points[i] = i;
        return points;
    }
};

std::vector<int> reisverschluss(int n)
{
    int half = n / 2;
    std::vector<int> a(half), b(n - half);
    for (int i = 0; i < a.size(); ++i)
        a[i] = i + 1;
    for (int i = 0; i < b.size(); ++i)
        b[i] = half + i + 1;
    std::reverse(a.begin(), a.end());
    std::reverse(b.begin(), b.end());
    std::vector<int> res;
    for (int i = 0; i < b.size(); ++i)
    {
        res.push_back(b[i]);
        if (i < a.size())
            res.push_back(a[i]);
    }
    return res;
}

class Calc
{
public:
    int n;
    std::vector<int> predictedPUWE;
    int d;
    Calc(int n, std::vector<int> predictedPUWE) : n(n), predictedPUWE(predictedPUWE), d(0) {}

    int main()
    {
        std::cout << "\n\n----------------------------------------\nCALC:  P(" << n << ")\n";

        std::vector<int> num = reisverschluss(n);

        P initStack(num);
        std::cout << "-- ";
        for (int i : num)
            std::cout << i << ' ';
        std::cout << "--\n";

        for (int i : predictedPUWE)
        {
            int a = find(initStack, i);
            if (std::find(predictedPUWE.begin(), predictedPUWE.end(), a) != predictedPUWE.end())
                return a;
        }
        return -1;
    }

private:
    int find(P stack, int wantedPUWE)
    {
        int stackPUWE = stack.history.size();
        if (stackPUWE < wantedPUWE)
        {
            for (int i : stack.getFlipIndexPoints())
            {
                P newStack = stack.copy();
                newStack.flip(i);
                int status = find(newStack, wantedPUWE);
                if (status == -1)
                    continue;
                else if (status == wantedPUWE)
                    return wantedPUWE;
            }
        }
        else if (stackPUWE == wantedPUWE)
        {
            if (stack.isValid())
            {
                std::cout << "\n";
                stack.printHistory();
                return stackPUWE;
            }
            else
                return -1;
        }
        else
            return -1;
        return -1;
    }
};

int main()
{
    std::vector<int> last_predictedPUWE = {4, 5, 6};
    std::vector<int> history = {4};
    for (int i = 8; i <= 100; ++i)
    {
        Calc calculator(i, last_predictedPUWE);
        auto start = std::chrono::high_resolution_clock::now();
        int puwe_i = calculator.main();
        auto end = std::chrono::high_resolution_clock::now();
        auto int_ms = std::chrono::duration_cast<std::chrono::milliseconds>(end - start);
        std::cout << "PUWE(" << i << ")=" << puwe_i << " in " << int_ms.count() << "ms calculated" << std::endl;
        history.push_back(puwe_i);
        if (history.back() == history[history.size() - 2])
        {
            last_predictedPUWE = {puwe_i + 1, puwe_i + 2, puwe_i + 3};
        }
        else
        {
            last_predictedPUWE = {puwe_i, puwe_i + 1, puwe_i + 2};
        }
    }
    return 0;
}